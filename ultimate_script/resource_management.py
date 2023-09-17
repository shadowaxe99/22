```python
import os
import psutil
import gc

class ResourceManagement:
    def __init__(self):
        self.process = psutil.Process(os.getpid())

    def get_memory_usage(self):
        """Returns the current memory usage of the script."""
        return self.process.memory_info().rss

    def get_disk_usage(self):
        """Returns the current disk usage."""
        return psutil.disk_usage('/')

    def get_cpu_usage(self):
        """Returns the current CPU usage."""
        return psutil.cpu_percent(interval=None)

    def dynamic_memory_allocation(self, size):
        """Allocates memory dynamically based on the required size."""
        try:
            data = [0] * size
            return data
        except MemoryError:
            print("Memory allocation failed. Trying to free up some space...")
            self.garbage_collection()
            return None

    def garbage_collection(self):
        """Performs garbage collection to free up memory."""
        gc.collect()

    def resource_pooling(self, resources):
        """Manages a pool of resources for efficient usage."""
        # This is a placeholder function. The actual implementation will depend on the type of resources being pooled.
        pass

    def optimize_performance(self):
        """Optimizes performance by managing resources efficiently."""
        # This is a placeholder function. The actual implementation will depend on the specific performance optimization techniques used.
        pass

resource_manager = ResourceManagement()
print("Memory Usage:", resource_manager.get_memory_usage())
print("Disk Usage:", resource_manager.get_disk_usage())
print("CPU Usage:", resource_manager.get_cpu_usage())
```
