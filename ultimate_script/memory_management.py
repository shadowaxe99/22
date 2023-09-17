```python
import gc
import psutil
import os

class MemoryManager:
    def __init__(self):
        self.process = psutil.Process(os.getpid())

    def get_memory_usage(self):
        """Returns the current memory usage of the script."""
        return self.process.memory_info().rss

    def free_memory(self):
        """Frees up memory by calling the garbage collector."""
        gc.collect()

    def optimize_memory(self, data):
        """Optimizes memory usage by converting data types of the input data."""
        for column in data.columns:
            if data[column].dtype == 'int64':
                data[column] = data[column].astype('int32')
            if data[column].dtype == 'float64':
                data[column] = data[column].astype('float32')
        return data

    def check_memory_threshold(self, threshold):
        """Checks if the current memory usage exceeds the given threshold."""
        if self.get_memory_usage() > threshold:
            self.free_memory()
            return True
        return False
```
