import json
import os
import time
import argparse
import requests
import pandas as pd
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

def load_config(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def select_from_list(items, prompt):
    if not items:
        raise ValueError(f"No items to select from for: {prompt}")
    print(prompt)
    for i, item in enumerate(items):
        print(f"{i+1}. {item}")
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(items):
                return items[choice - 1]
            else:
                print(f"Please enter a number between 1 and {len(items)}")
        except ValueError:
            print("Please enter a valid number")

def select_model(config):
    print("Select a model provider:")
    for i, provider in enumerate(config['model_providers']):
        print(f"{i+1}. {provider['name']}")
    provider_choice = int(input("Enter the number of your choice: ")) - 1
    selected_provider = config['model_providers'][provider_choice]

    print(f"\nSelect a model from {selected_provider['name']}:")
    for i, model in enumerate(selected_provider['models']):
        print(f"{i+1}. {model['model_alias']} ({model['name']})")
    model_choice = int(input("Enter the number of your choice: ")) - 1
    selected_model = selected_provider['models'][model_choice]

    return selected_model

def get_api_info(model_name, config):
    api_info = load_config('api_private.json')

    provider = None
    for p in config['model_providers']:
        if any(m['name'] == model_name for m in p['models']):
            provider = p['name']
            break

    if not provider:
        raise ValueError(f"No provider found for model: {model_name}")

    if provider not in api_info:
        raise ValueError(f"No API information found for provider: {provider}")

    return {
        'api_key': api_info[provider]['api_key'],
        'endpoint': api_info[provider]['endpoint'],
        'provider': provider
    }


def fetch_response(conf, config):
    start_time = time.time()
    api_info = get_api_info(conf['model'], config)
    headers = {
        'Authorization': f"Bearer {api_info['api_key']}",
        'Content-Type': 'application/json'
    }

    payload = {
        "model": conf['model'],
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": conf['prompt']}
        ],
        **conf['parameters']
    }

    response = requests.post(api_info['endpoint'], headers=headers, json=payload)
    end_time = time.time()

    if response.status_code == 200:
        response_json = response.json()
        return {
            "model": conf['model'],
            "model_alias": conf['model_alias'],
            "task_type": conf['task_type'],
            "category": conf['category'],
            "prompt": conf['prompt'],
            "language": conf['language'],
            "temperature": conf['parameters'].get('temperature', 'N/A'),
            "max_tokens": conf['parameters'].get('max_tokens', 'N/A'),
            "top_p": conf['parameters'].get('top_p', 'N/A'),
            "frequency_penalty": conf['parameters'].get('frequency_penalty', 'N/A'),
            "presence_penalty": conf['parameters'].get('presence_penalty', 'N/A'),
            "response_text": response_json["choices"][0]["message"]["content"],
            "timestamp": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time)),
            "response_time": end_time - start_time,
            "total_tokens": response_json.get("usage", {}).get("total_tokens", "N/A")
        }
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

def run_experiment(configs, full_config):
    results = []
    total_calls = sum(conf['call_count'] for conf in configs)
    with ThreadPoolExecutor(max_workers=min(total_calls, 20)) as executor:
        futures = []
        for conf in configs:
            futures.extend([executor.submit(fetch_response, conf, full_config) for _ in range(conf['call_count'])])
        for future in tqdm(as_completed(futures), total=total_calls, desc="Processing API calls"):
            result = future.result()
            if result:
                results.append(result)
    return results

def main():
    parser = argparse.ArgumentParser(description="Language Model Experiment")
    parser.add_argument("--config", default="config.json", help="Path to configuration file")
    parser.add_argument("--model", help="Model to use")
    parser.add_argument("--task_type", help="Type of task")
    parser.add_argument("--task", help="Specific task")
    parser.add_argument("--parameter_set", help="Parameter set to use")
    parser.add_argument("--language", help="Language for the task")
    parser.add_argument("--call_count", type=int, help="Number of API calls")
    args = parser.parse_args()

    config = load_config(args.config)

    # Select model
    if args.model:
        selected_model = next((model for provider in config['model_providers'] for model in provider['models'] if model['name'] == args.model), None)
        if not selected_model:
            raise ValueError(f"Model '{args.model}' not found in configuration.")
    else:
        selected_model = select_model(config)


    # Select task type and category
    if args.task_type and args.category:
        task_type = next(tt for tt in config['task_types'] if tt['name'] == args.task_type)
        category = next(c for c in task_type['categories'] if c['name'] == args.category)
    else:
        task_type = select_from_list([tt['name'] for tt in config['task_types']], "Select a task type:")
        task_type = next(tt for tt in config['task_types'] if tt['name'] == task_type)
        category = select_from_list(task_type['categories'], "Select a specific category:")

    # Select parameter set
    if args.parameter_set:
        parameter_set = args.parameter_set
    else:
        parameter_sets = [ps['name'] for ps in config['parameter_sets']]
        if not parameter_sets:
            raise ValueError("No parameter sets found in the configuration file.")
        parameter_set = select_from_list(parameter_sets, "Select a parameter set:")

    # Find the selected parameter set
    selected_params = next((ps for ps in config['parameter_sets'] if ps['name'] == parameter_set), None)
    if selected_params is None:
        raise ValueError(f"Parameter set '{parameter_set}' not found in the configuration file.")

    # Select language
    language = args.language if args.language else select_from_list(config['languages'], "Select a language:")

    # Select call count
    call_count = args.call_count if args.call_count else select_from_list(config['call_counts'], "Select the number of API calls:")

    # Prepare configuration
    experiment_config = {
        "model": selected_model['name'],
        "model_alias": selected_model['model_alias'],
        "task_type": task_type['name'],
        "category": category['name'],
        "prompt": category['prompt'],
        "language": language,
        "parameters": selected_params,
        "call_count": call_count
    }


    # Run experiment
    results = run_experiment([experiment_config], config)


    # Save results
    output_folder = "output_files"
    os.makedirs(output_folder, exist_ok=True)
    output_file = os.path.join(output_folder, "api_responses.csv")

    file_exists = os.path.isfile(output_file)
    results_df = pd.DataFrame(results)

    # Ensure all required columns are present
    required_columns = ["model_alias", "temperature", "top_p", "frequency_penalty", "presence_penalty", "response_text", "category"]
    for col in required_columns:
        if col not in results_df.columns:
            results_df[col] = ""  # or some default value

    # Reorder columns to match R script expectations
    results_df = results_df[required_columns + [col for col in results_df.columns if col not in required_columns]]

    results_df.to_csv(output_file, mode='a', header=not file_exists, index=False)
    print(f"Results appended to {output_file}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
        import traceback
        traceback.print_exc()