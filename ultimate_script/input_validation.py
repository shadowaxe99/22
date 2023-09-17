```python
import os
import pandas as pd

SUPPORTED_FILE_FORMATS = ['csv', 'xlsx', 'xls']

def validate_file_format(file_path):
    file_extension = os.path.splitext(file_path)[1][1:]
    if file_extension not in SUPPORTED_FILE_FORMATS:
        raise ValueError(f"Unsupported file format. Supported formats are: {', '.join(SUPPORTED_FILE_FORMATS)}")

def validate_file_exists(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist.")

def validate_data_schema(data):
    required_columns = ['FirstName', 'LastName', 'Email', 'Phone']
    missing_columns = [col for col in required_columns if col not in data.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(missing_columns)}")

def validate_data_values(data):
    if data.isnull().values.any():
        raise ValueError("Data contains null values.")
    if not data['Email'].str.contains('@').all():
        raise ValueError("Invalid email addresses detected.")
    if not data['Phone'].str.isdigit().all():
        raise ValueError("Invalid phone numbers detected.")

def validate_input_file(file_path):
    validate_file_exists(file_path)
    validate_file_format(file_path)
    data = pd.read_csv(file_path) if file_path.endswith('.csv') else pd.read_excel(file_path)
    validate_data_schema(data)
    validate_data_values(data)
    return data
```