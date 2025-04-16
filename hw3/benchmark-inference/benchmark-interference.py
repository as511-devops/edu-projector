import time
from concurrent.futures import ProcessPoolExecutor
import multiprocessing

# Simulated inference function that performs CPU-bound work.
def dummy_inference(x):
    # For this example, "inference" will compute the sum of squares for a range of numbers
    result = sum(i * i for i in range(1000000))
    return result

# Benchmark inference sequentially (single process)
def benchmark_single(inputs):
    start_time = time.perf_counter()
    # Process each input one by one.
    for x in inputs:
        _ = dummy_inference(x)
    end_time = time.perf_counter()
    return end_time - start_time

# Benchmark inference in parallel using multiple processes.
def benchmark_multi(inputs, max_workers=None):
    start_time = time.perf_counter()
    # Create a process pool (if max_workers is None, it uses os.cpu_count())
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        # Map the dummy_inference function to the inputs in parallel.
        list(executor.map(dummy_inference, inputs))
    end_time = time.perf_counter()
    return end_time - start_time

if __name__ == '__main__':
    # Define a set of inference tasks.
    num_tasks = 20
    inputs = list(range(num_tasks))
    
    # Measure single-process (sequential) inference time.
    single_time = benchmark_single(inputs)
    
    # Measure multi-process (parallel) inference time.
    num_workers = multiprocessing.cpu_count()
    multi_time = benchmark_multi(inputs, max_workers=num_workers)
    
    # Report the results.
    print("Single-process inference time: {:.4f} seconds".format(single_time))
    print("Multi-process inference time ({} workers): {:.4f} seconds".format(num_workers, multi_time))
