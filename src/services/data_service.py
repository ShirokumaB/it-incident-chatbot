import pandas as pd
import os

def load_data():
    """
    Loads incident data from the mock CSV file.
    In a real scenario, this would connect to a PostgreSQL database.
    """
    # Get the absolute path to the data file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(current_dir))
    data_path = os.path.join(project_root, 'data', 'mock_incidents.csv')
    
    try:
        df = pd.read_csv(data_path)
        # Ensure we handle missing values as '-' for consistency with the UI logic
        df = df.fillna('-')
        return df
    except FileNotFoundError:
        print(f"Error: Data file not found at {data_path}")
        return pd.DataFrame() # Return empty DataFrame on error
