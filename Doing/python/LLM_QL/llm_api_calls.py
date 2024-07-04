"""
This script fetches responses from an API based on predefined configurations and saves each response with metadata into a CSV file.

It reads configuration settings from JSON files, sends API requests using defined parameters, processes the responses, and outputs the results in a structured format.

The function `fetch_response()` is used to send individual API requests and collect relevant details for each response. The script utilizes a ThreadPoolExecutor to execute multiple requests in parallel for efficiency.

The final results are stored in a pandas DataFrame and saved into a CSV file with the name derived from the selected configuration, along with timestamps, response times, and token counts.
"""

import requests
import json
import pandas as pd
import os
import time
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

# Check if a private configuration file exists
config_file = 'config_private.json' if os.path.isfile('config_private.json') else 'config.json'

# Load configurations based on user selection from the JSON file.
with open(config_file, encoding='utf-8') as f:
    config = json.load(f)

# Display available configurations for user selection and take input
print("Available Configurations:")
for i, conf in enumerate(config['configurations']):
    print(f"{i+1}. {conf['name']}")
selection = int(input("Select configuration: ")) - 1
selected_config = config['configurations'][selection]

# Set request parameters like endpoint URL, headers and payload template based on selected configuration.
url = selected_config['endpoint']
headers = {
    'Authorization': f"Bearer {selected_config['api_key']}",
    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
    'Content-Type': 'application/json'
}
payload_template = {
    "model": selected_config["model"],
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": selected_config["prompt"]}
    ]
}

# Initialize storage for results
results = []

def fetch_response():
    """
    Function to process API requests, record responses and related information.

    This function records the start time of an API call, sends a POST request with headers and data payload based on the configuration,
    processes the JSON response from the API to extract useful details such as timestamp, response time etc.,
    and returns these data in a structured format for further processing.

        "model": The name of the used model;
        "prompt": The user's request (i.e., question or command);
        "temperature": The parameter for temperature in the model, default to 0.5;
        "max_tokens": The maximum number of tokens that will limit the output length as a text block;
        "top_p": Used to control the cumulative probability in the continuous probability distribution, defaults no punishment (1.0);
        "frequency_penalty": Controls repetition by penalizing repeated words and phrases, defaults no punishment (0.0);
        "presence_penalty": Controls the generation of new content by penalizing unrelated new content, defaults no punishment (0.0);
        "response_text": API response text;
        "timestamp": The timestamp when the request was started;
        "response_time": The total time interval from the start of the request to the API returning a response;
        "total_tokens": The total number of tokens in the API response, including model-generated output and any additional data or metadata.
    """
    # Record the start time of the API call
    start_time = time.time()

    # Send a POST request to the URL with headers and data payload based on selected configuration.
    response = requests.post(url, headers=headers, data=json.dumps(payload_template))
    response_json = response.json()
    # Record the end time of the API call
    end_time = time.time()

    # Process the JSON response from the API and extract useful details such as timestamp, response time etc.
    response_data = []
    if "choices" in response.json():
        for choice in response_json["choices"]:
            result = {
                "model": selected_config["model"],
                "model_alias":selected_config["model_alias"],
                "type":selected_config["type"],
                "prompt": selected_config["prompt"],
                "temperature": selected_config["temperature"],
                "max_tokens": selected_config["max_tokens"],
                "top_p": selected_config.get("top_p", 1.0),
                "frequency_penalty": selected_config.get("frequency_penalty", 0.0),
                "presence_penalty": selected_config.get("presence_penalty", 0.0),
                "response_text": choice["message"]["content"],
                "timestamp": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time)),
                "response_time": end_time - start_time,
                "total_tokens": response_json.get("usage", {}).get("total_tokens", "N/A")
            }
            response_data.append(result)
    else:
        print(f"API response missing 'choices' key: {response.json()}")
    return response_data

# Use ThreadPoolExecutor to make multiple requests in parallel for efficiency
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(fetch_response) for _ in range(selected_config["call_count"])]
    for future in tqdm(as_completed(futures), total=selected_config["call_count"], desc="Processing API calls"):
        results.extend(future.result())

# Create output folder (if it doesn't exist)
output_folder = "output_files"
os.makedirs(output_folder, exist_ok=True)

# Generate output file path based on configuration name
output_file = os.path.join(output_folder, "api_responses.csv")

# Check if the CSV file exists and decide whether to write headers or not.
write_header = not os.path.isfile(output_file)

# Add the configuration name as part of each result
for result in results:
    result["config_name"] = selected_config["name"]

# Save the collected responses into a structured CSV file format
results_df = pd.DataFrame(results)
results_df = results_df[["config_name"] + [col for col in results_df.columns if col != "config_name"]]  # Put config_name as the first column
results_df.to_csv(output_file, mode='a', index=False, header=write_header)

print(f"Requests and responses saved to {output_file}.")
