# StreamingDataset Conversion

This script converts a static dataset into a streaming-capable format using a `StreamingDataset` wrapper. This is useful when working with large datasets that cannot fit entirely into memory or when training models that require continuous data flow.

## 📦 What It Does

- Loads a dataset from disk (e.g. CSV, JSON, or image folders)
- Wraps the dataset into a `StreamingDataset`-style generator or iterator
- Streams data sample-by-sample instead of loading everything at once
- Prepares data for memory-efficient model training or evaluation

## 📚 How It Works

1. **Data Source**  
   The input dataset can be in CSV, JSON, Parquet, or any format supported by Pandas or native Python I/O.

2. **Streaming Dataset Class**  
   Implements a custom `StreamingDataset` class (or uses one from a framework like PyTorch or MosaicML) that yields data items on-the-fly.

3. **No Full Dataset in Memory**  
   Only one or a few samples are kept in memory at a time, ideal for large-scale workloads.

## 🔧 Example Usage

