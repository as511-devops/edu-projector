## TL;DR
✅ Generates synthetic data

✅ Saves it as Parquet

✅ Loads it using Hugging Face datasets in streaming mode

✅ Prints the first 5 streamed samples

## Output example
```bash
📦 Generating synthetic dataset...
✅ Saved dataset to data/train.parquet
🌊 Loading dataset in streaming mode...
🔍 First 5 streamed samples:
{'feature1': 0.0067, 'feature2': 0.3225, 'label': 1}
{'feature1': 0.5448, 'feature2': 0.4295, 'label': 1}
{'feature1': 0.1787, 'feature2': 0.1798, 'label': 1}
{'feature1': 0.5507, 'feature2': 0.7426, 'label': 1}
{'feature1': 0.3801, 'feature2': 0.0328, 'label': 0}
```
