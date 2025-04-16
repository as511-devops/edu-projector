import pandas as pd
import numpy as np
import os
import time

# Set a fixed seed for reproducibility
np.random.seed(42) # 42 = answer to all question :D

# Generate a sample DataFrame with 1 million rows and 10 columns of random floats
n_rows = 1_000_000
n_cols = 20
df = pd.DataFrame(np.random.rand(n_rows, n_cols), columns=[f'col{i}' for i in range(n_cols)])

# Define formats to test: (format name, save function, load function, file extension)
formats = [
    ("CSV",     lambda df, f: df.to_csv(f, index=False), pd.read_csv, ".csv"),
    ("JSON",    lambda df, f: df.to_json(f), pd.read_json, ".json"),
    ("Parquet", lambda df, f: df.to_parquet(f), pd.read_parquet, ".parquet"),
    ("Feather", lambda df, f: df.to_feather(f), pd.read_feather, ".feather"),
    ("Pickle",  lambda df, f: df.to_pickle(f), pd.read_pickle, ".pkl"),
]

results = []

for name, save_func, load_func, ext in formats:
    filename = f"temp{ext}"
    
    # Time saving
    start_save = time.perf_counter()
    save_func(df, filename)
    save_time = time.perf_counter() - start_save

    # Get file size in MB
    file_size = os.path.getsize(filename) / (1024 * 1024)

    # Time loading
    start_load = time.perf_counter()
    df_loaded = load_func(filename)
    load_time = time.perf_counter() - start_load

    results.append((name, save_time, load_time, file_size))
    
    # Clean up the file
    os.remove(filename)

# Print the benchmark results
print(f"{'Format':<10}{'Save Time (s)':<15}{'Load Time (s)':<15}{'Size (MB)':<10}")
for name, st, lt, size in results:
    print(f"{name:<10}{st:<15.4f}{lt:<15.4f}{size:<10.2f}")
