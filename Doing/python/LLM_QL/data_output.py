import pandas as pd
import os

# 读取 CSV 文件
csv_file = 'output_files/api_responses.csv'
df = pd.read_csv(csv_file)

# 获取所有唯一的配置名称
config_names = df['config_name'].unique()

# 提示用户选择配置
print("可用的配置：")
for i, name in enumerate(config_names):
    print(f"{i+1}. {name}")
selection = int(input("输入你想使用的配置编号: ")) - 1
selected_config = config_names[selection]

# 过滤出特定配置名称的所有 response_text
filtered_responses = df[df['config_name'] == selected_config]['response_text']

# 创建输出文件夹（如果不存在）
output_dir = 'output_txt_files'
os.makedirs(output_dir, exist_ok=True)

# 导出到 TXT 文件
output_file = os.path.join(output_dir, f"{selected_config}_responses.txt")
with open(output_file, 'w', encoding='utf-8') as f:
    for response in filtered_responses:
        f.write(response + '\n')

print(f"配置 '{selected_config}' 的所有 response_text 已导出到 {output_file}")
