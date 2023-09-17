```python
import logging
import sys

# Define a custom exception
class DataProcessingError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Set up logging
logging.basicConfig(filename='error_log.log', level=logging.ERROR)

def handle_error(e, message):
    logging.error(message)
    raise DataProcessingError(message) from e

def process_data(input_file):
    try:
        # Assume process_file is a function that processes the data
        process_file(input_file)
    except FileNotFoundError as e:
        handle_error(e, f"File {input_file} not found.")
    except PermissionError as e:
        handle_error(e, f"Insufficient permissions to read file {input_file}.")
    except Exception as e:
        handle_error(e, f"An unexpected error occurred while processing file {input_file}.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python error_handling.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    process_data(input_file)
```