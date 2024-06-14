"""
This Python script performs operations on API responses from different configurations.

Functions included:
- Reading CSV file containing API responses.
- Extracting unique configuration names to facilitate user selection.
- Displaying available configurations for users and prompting them for input.
- Filtering responses that belong to a selected configuration based on 'config_name' column.
- Creating an output folder if it doesn't exist, ensuring proper file organization and storage.
- Defining the name of the text file where filtered responses will be saved after operations.
- Writing filtered responses to a TXT file using UTF-8 encoding for compatibility across different systems.
- Printing confirmation message indicating successful export of selected configuration's responses.

Usage:
1. Execute script
2. A list of available configurations is displayed; choose one by entering its number.
3. The script filters the API responses for that configuration and saves them in a TXT file named after the config_name, with '_responses.txt' appended to it.
4. Confirmation message prints out the path where responses have been exported.

Dependencies:
- pandas: For data manipulation and analysis.
- os: To interact with the operating system.

"""

# Import necessary libraries and tools for file operations
import pandas as pd # Pandas is a library used for data manipulation and analysis
import os           # OS module provides functions for interacting with the operating system

# Read CSV file containing API responses
csv_file = 'output_files/api_responses.csv'
df = pd.read_csv(csv_file)

# Extract unique configuration names from the dataset to facilitate user selection
config_names = df['config_name'].unique()

# Display available configurations to users and prompt them for input
print("Available configurations:")
for i, name in enumerate(config_names):
    print(f"{i+1}. {name}")
selection = int(input("Enter the number corresponding to your desired configuration: ")) - 1 # -1 because list indexes start at zero
selected_config = config_names[selection]

# Filter responses that belong to the selected configuration based on 'config_name' column
filtered_responses = df[df['config_name'] == selected_config]['response_text']

# Create an output folder if it doesn't already exist, ensuring proper file organization and storage
output_dir = 'output_txt_files'
os.makedirs(output_dir, exist_ok=True)

# Define the name of the text file where responses will be saved after filtering operations
output_file = os.path.join(output_dir, f"{selected_config}_responses.txt")

# Write filtered responses to a TXT file using UTF-8 encoding for compatibility across different systems.
with open(output_file, 'w', encoding='utf-8') as f:
    for response in filtered_responses:
        f.write(response + '\n')

# Print confirmation message indicating the successful export of selected configuration's responses
print(f"Responses from configuration '{selected_config}' have been exported to {output_file}")
