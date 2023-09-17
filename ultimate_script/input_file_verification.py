```python
import os
import hashlib

SUPPORTED_FILE_FORMATS = ['csv', 'xlsx', 'xls']
MAX_FILE_SIZE = 1024 * 1024 * 1024  # 1GB

def verify_file(file_path):
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    # Check if file size is within the limit
    if os.path.getsize(file_path) > MAX_FILE_SIZE:
        raise Exception(f"The file {file_path} exceeds the maximum file size limit.")

    # Check if file format is supported
    if file_path.split('.')[-1].lower() not in SUPPORTED_FILE_FORMATS:
        raise Exception(f"The file {file_path} is not a supported file format.")

    # Verify file integrity
    if not verify_checksum(file_path):
        raise Exception(f"The file {file_path} failed the checksum verification.")

def calculate_checksum(file_path, algorithm='sha256'):
    hash_obj = hashlib.new(algorithm)

    with open(file_path, 'rb') as f:
        while True:
            data = f.read(8192)
            if not data:
                break
            hash_obj.update(data)

    return hash_obj.hexdigest()

def verify_checksum(file_path, algorithm='sha256'):
    stored_checksum = get_stored_checksum(file_path)
    calculated_checksum = calculate_checksum(file_path, algorithm)

    return stored_checksum == calculated_checksum

def get_stored_checksum(file_path):
    # This function should be implemented to retrieve the stored checksum of the file.
    # The implementation depends on how and where the checksums are stored.
    pass
```