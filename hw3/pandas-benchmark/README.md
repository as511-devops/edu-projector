# Benchmarking Pandas Data Formats

This project benchmarks various file formats supported by Pandas in terms of data saving and loading performance. The goal is to measure both the time required to save/load a DataFrame as well as the resulting file sizes for different formats such as CSV, JSON, Parquet, Feather, and Pickle.

## Overview

To ensure that each benchmark is run on the exact same logical data, we generate a synthetic DataFrame using a fixed random seed. This guarantees reproducibility and fairness across all the formats.

### Data Generation

We generate our synthetic DataFrame with the following ideas:

- **Numeric Data:**  
  Generate random floating-point numbers using:
  ```python
  np.random.rand(n_rows, n_cols)

### Results
Format    Save Time (s)  Load Time (s)  Size (MB) 
CSV       16.9896        1.4019         367.54    
JSON      1.7999         8.0413         415.38    
Parquet   0.3768         0.1098         157.94    
Feather   0.0955         0.0442         152.63    
Pickle    0.0416         0.0515         152.59
