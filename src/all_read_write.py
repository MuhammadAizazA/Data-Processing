import yaml
import json
import pandas as pd

def read_yaml(file_path):
    with open(file_path, "r") as file:
        data = yaml.safe_load(file)
    return data

def write_yaml(file_path, data):
    with open(file_path, "w") as file:
        yaml.dump(data, file)

def read_json(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data

def write_json(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file)

def read_excel(file_path):
    data = pd.read_excel(file_path, engine='openpyxl')
    return data

def write_excel(file_path, data):
    data.to_excel(file_path, index=False)

def read_csv(file_path):
    data = pd.read_csv(file_path)
    return data

def write_csv(file_path, data):
    data.to_csv(file_path, index=False)

def read_data(file_path, file_format):
    if file_format == 'yaml':
        return read_yaml(file_path)
    elif file_format == 'json':
        return read_json(file_path)
    elif file_format == 'excel':
        return read_excel(file_path)
    elif file_format == 'csv':
        return read_csv(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_format}")

def write_data(file_path, data, file_format):
    if file_format == 'yaml':
        write_yaml(file_path, data)
    elif file_format == 'json':
        write_json(file_path, data)
    elif file_format == 'excel':
        write_excel(file_path, data)
    elif file_format == 'csv':
        write_csv(file_path, data)
    else:
        raise ValueError(f"Unsupported file format: {file_format}")

# Read Example:
file_path_to_read = "data/all.yaml"
file_format_to_read = "yaml"
data_to_read = read_data(file_path_to_read, file_format_to_read)
print(f"Read data:\n{data_to_read}")

# Write Example:
file_path_to_write = "output.yaml"
file_format_to_write = "yaml"
data_to_write = {"example_key": "example_value"}
write_data(file_path_to_write, data_to_write, file_format_to_write)
print(f"Data written to {file_path_to_write}")
