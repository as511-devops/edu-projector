# Inference Benchmark: Single vs Multi-Process

This script benchmarks the performance difference between running a simulated inference workload using a single process (sequential execution) versus multiple processes (parallel execution).

## �� What It Does

- Simulates a CPU-bound "inference" task by computing the sum of squares up to 1,000,000.
- Runs this task multiple times over a list of dummy inputs.
- Measures and compares:
  - 🕒 Time taken when run **sequentially** (one by one)
  - 🕒 Time taken when run **in parallel** (using multiple processes)
- Prints the total execution time for both methods.

## 🚀 How It Works

- **Single-process mode**: Runs inference tasks one after another in a loop.
- **Multi-process mode**: Uses Python's `concurrent.futures.ProcessPoolExecutor` to run tasks in parallel using all available CPU cores.

## ⚙️ Configuration

- Number of tasks: 20 (can be changed in the script)
- Each task runs the same dummy computation
- Number of processes used in parallel: equal to the number of CPU cores (auto-detected)

## 📈 Example Output
Single-process inference time: 0.6081 seconds
Multi-process inference time (16 workers): 0.1116 seconds
