# Data Validation DBT Project

This project is designed to perform data validation processes using dbt (data build tool) and Python. It includes configurations for connecting to various databases, defining tables for validation, and orchestrating validation tasks.

## Project Structure

- **config.yaml**: Contains configuration settings for database connections and table definitions for data validation processes.
- **README.md**: Documentation for the project, including setup instructions and usage guidelines.
- **results/**: Directory to store the output results of the data validation processes.
- **src/**: Contains the main Python scripts for data validation.
  - **main.py**: The main entry point for the data validation scripts.
  - **utils.py**: Utility functions that support the main data validation processes.
- **dbt/**: Contains dbt-related files and directories.
  - **models/**: SQL models for transforming raw data into structured formats.
    - **customer.sql**: Defines the SQL model for customer data.
  - **seeds/**: Directory for seed data files.
  - **snapshots/**: Directory for snapshot definitions that track historical changes in the data.
  - **dbt_project.yml**: Configuration for the dbt project.
  - **profiles.yml**: Connection profiles for dbt.
- **requirements.txt**: Lists the Python dependencies required for the project.

## Setup Instructions

1. Clone the repository to your local machine.
2. Install the required Python packages by running:
   ```
   pip install -r requirements.txt
   ```
3. Configure your database connections in `config.yaml` and `dbt/profiles.yml`.
4. Run the data validation scripts using:
   ```
   python src/main.py
   ```
5. Check the `results/` directory for output results.

## Usage Guidelines

- Modify the `config.yaml` file to adjust database settings and table definitions as needed.
- Use the `src/utils.py` file to add any utility functions that may assist in data validation.
- Update the dbt models in the `dbt/models/` directory to reflect any changes in data transformation logic.

For more detailed information on dbt, please refer to the official dbt documentation.