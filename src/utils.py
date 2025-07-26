def load_data(file_path):
    # Function to load data from a specified file path
    import pandas as pd
    return pd.read_csv(file_path)

def validate_data(df, validation_rules):
    # Function to validate data based on specified rules
    for column, condition in validation_rules.items():
        if not df[column].apply(condition).all():
            raise ValueError(f"Validation failed for column: {column}")
    return True

def transform_data(df, transformations):
    # Function to apply transformations to the data
    for column, func in transformations.items():
        df[column] = df[column].apply(func)
    return df

def save_results(df, output_path):
    # Function to save the results to a specified output path
    df.to_csv(output_path, index=False)