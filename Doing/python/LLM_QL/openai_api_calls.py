import requests
import json
import pandas as pd
import os
import time
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

# 检查是否存在私有配置文件
config_file = 'config_private.json' if os.path.isfile('config_private.json') else 'config.json'

# 加载配置文件
with open(config_file, encoding='utf-8') as f:
    config = json.load(f)

# 提示用户选择配置
print("可用的配置：")
for i, conf in enumerate(config['configurations']):
    print(f"{i+1}. {conf['name']}")
selection = int(input("输入你想使用的配置编号: ")) - 1
selected_config = config['configurations'][selection]

# 设置请求参数
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

# 初始化存储结果的列表
results = []

def fetch_response():
    start_time = time.time()
    response = requests.post(url, headers=headers, data=json.dumps(payload_template))
    end_time = time.time()

    response_json = response.json()
    response_data = []
    if "choices" in response_json:
        for choice in response_json["choices"]:
            result = {
                "model": selected_config["model"],
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
        print(f"API 响应中缺少 'choices' 键: {response_json}")
    return response_data

# 使用 ThreadPoolExecutor 进行并发请求
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(fetch_response) for _ in range(selected_config["call_count"])]
    for future in tqdm(as_completed(futures), total=selected_config["call_count"], desc="Processing API calls"):
        results.extend(future.result())

# 创建输出文件夹（如果不存在）
output_folder = "output_files"
os.makedirs(output_folder, exist_ok=True)

# 生成输出文件路径
output_file = os.path.join(output_folder, "api_responses.csv")

# 检查文件是否存在，决定是否写入表头
write_header = not os.path.isfile(output_file)

# 将配置名称添加到结果中
for result in results:
    result["config_name"] = selected_config["name"]

# 将结果保存到 CSV 文件中
results_df = pd.DataFrame(results)
results_df = results_df[["config_name"] + [col for col in results_df.columns if col != "config_name"]]  # 将 config_name 放到第一列
results_df.to_csv(output_file, mode='a', index=False, header=write_header)

print(f"请求和响应已保存到 {output_file}。")
