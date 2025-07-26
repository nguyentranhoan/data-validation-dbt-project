# File: /data-validation-dbt-project/data-validation-dbt-project/src/main.py

import yaml
import os
from utils import validate_data

def load_config(config_path):
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

def main():
    config = load_config(os.path.join(os.path.dirname(__file__), '../config.yaml'))
    
    # Example of how to access the tables defined in the config
    for table in config['tables']:
        print(f"Validating table: {table['name']}")
        validate_data(table)

if __name__ == "__main__":
    main()