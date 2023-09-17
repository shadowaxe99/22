```python
import time
import csv
import pandas as pd
from memory_profiler import memory_usage
from ultimate_script.input_validation import validate_input
from ultimate_script.error_handling import handle_error
from ultimate_script.memory_management import manage_memory
from ultimate_script.performance_optimization import optimize_performance

PERFORMANCE_THRESHOLD = 1.0  # seconds

def test_performance(input_file):
    start_time = time.time()
    mem_usage_before = memory_usage()[0]

    try:
        validate_input(input_file)
        data = pd.read_csv(input_file)
        sorted_data = optimize_performance(data)
    except Exception as e:
        handle_error(e)

    end_time = time.time()
    mem_usage_after = memory_usage()[0]

    time_taken = end_time - start_time
    mem_used = mem_usage_after - mem_usage_before

    manage_memory()

    if time_taken > PERFORMANCE_THRESHOLD:
        print(f"Performance test failed. Time taken: {time_taken} seconds")
    else:
        print(f"Performance test passed. Time taken: {time_taken} seconds")

    print(f"Memory used: {mem_used} MB")

if __name__ == "__main__":
    test_performance("sample.csv")
```