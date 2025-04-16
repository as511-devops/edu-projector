import os
import random
import pandas as pd
from datasets import load_dataset

# Step 1: Generate synthetic data and save as Parquet
os.makedirs("data", exist_ok=True)
parquet_path = "data/train.parquet"

if not os.path.exists(parquet_path):
    print("📦 Generating synthetic dataset...")

    num_samples = 10000
    df = pd.DataFrame({
        "feature1": [round(random.uniform(0, 1), 4) for _ in range(num_samples)],
        "feature2": [round(random.uniform(0, 1), 4) for _ in range(num_samples)],
        "label": [random.randint(0, 1) for _ in range(num_samples)],
    })

    df.to_parquet(parquet_path, index=False)
    print(f"✅ Saved dataset to {parquet_path}")
else:
    print(f"🔁 Using existing dataset at {parquet_path}")

# Step 2: Load with Hugging Face in streaming mode
print("🌊 Loading dataset in streaming mode...")
streaming_ds = load_dataset(
    "parquet",
    data_files=parquet_path,
    split="train",
    streaming=True
)

# Step 3: Print the first 5 samples
print("🔍 First 5 streamed samples:")
for i, row in enumerate(streaming_ds):
    print(row)
    if i == 4:
        break
