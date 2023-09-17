```python
import os
import pandas as pd
from openpyxl import load_workbook

SUPPORTED_FILE_FORMATS = ['csv', 'xlsx', 'xls']

def check_file_format(file_path):
    file_extension = os.path.splitext(file_path)[1][1:]
    if file_extension not in SUPPORTED_FILE_FORMATS:
        raise ValueError(f"Unsupported file format: {file_extension}. Supported formats are: {SUPPORTED_FILE_FORMATS}")

def check_compatibility_with_libraries(file_path):
    file_extension = os.path.splitext(file_path)[1][1:]
    try:
        if file_extension == 'csv':
            df = pd.read_csv(file_path)
        else:
            df = pd.read_excel(file_path)
        return True
    except Exception as e:
        print(f"Error while reading the file with pandas: {str(e)}")
        return False

def check_compatibility_with_os(file_path):
    try:
        with open(file_path, 'r') as file:
            file.read()
        return True
    except Exception as e:
        print(f"Error while opening the file: {str(e)}")
        return False

def run_compatibility_tests(file_path):
    check_file_format(file_path)
    if not check_compatibility_with_libraries(file_path):
        print(f"File {file_path} is not compatible with pandas library.")
    if not check_compatibility_with_os(file_path):
        print(f"File {file_path} is not compatible with the current operating system.")
```
