```python
import os
import hashlib
from cryptography.fernet import Fernet

class SecurityMeasures:
    def __init__(self):
        self.key = os.getenv('ENCRYPTION_KEY')
        self.cipher_suite = Fernet(self.key)

    def encrypt_data(self, data):
        """Encrypts the given data using Fernet symmetric encryption."""
        encrypted_data = self.cipher_suite.encrypt(data)
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        """Decrypts the given data using Fernet symmetric encryption."""
        decrypted_data = self.cipher_suite.decrypt(encrypted_data)
        return decrypted_data

    def hash_file(self, file_path, algorithm='sha256'):
        """Generates a hash for the given file using the specified algorithm."""
        hash_obj = hashlib.new(algorithm)

        with open(file_path, 'rb') as file:
            while chunk := file.read(8192):
                hash_obj.update(chunk)

        return hash_obj.hexdigest()

    def verify_file_integrity(self, file_path, expected_hash, algorithm='sha256'):
        """Verifies the integrity of the given file by comparing its hash with the expected hash."""
        actual_hash = self.hash_file(file_path, algorithm)
        return actual_hash == expected_hash

    def secure_file_access(self, file_path, access_mode):
        """Secures file access by checking for sufficient permissions before opening the file."""
        if not os.access(file_path, os.R_OK):
            raise PermissionError(f"Read access to {file_path} is denied.")
        if 'w' in access_mode and not os.access(file_path, os.W_OK):
            raise PermissionError(f"Write access to {file_path} is denied.")

        return open(file_path, access_mode)
```