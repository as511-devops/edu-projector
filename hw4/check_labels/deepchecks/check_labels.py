import pandas as pd
from deepchecks.nlp import TextData
from deepchecks.nlp.suites import data_integrity, train_test_validation

# Load your labeled CSV
df = pd.read_csv("banking_support_500_ukr.csv")

# Prepare lists of texts and labels
texts = df["text"].astype(str).tolist()
labels = df["category"].astype(str).tolist()

# Create Deepchecks TextData with task_type
td = TextData(raw_text=texts, label=labels, task_type="text_classification")

# Run Data Integrity suite
integrity_suite = data_integrity()
result_data = integrity_suite.run(td)
result_data.save_as_html("deepchecks_data_integrity.html")

# (Optional) Train‑Test split for validation
n = len(texts)
train_size = int(0.8 * n)
train_td = TextData(raw_text=texts[:train_size], label=labels[:train_size], task_type="text_classification")
test_td  = TextData(raw_text=texts[train_size:], label=labels[train_size:], task_type="text_classification")

tt_suite = train_test_validation()
result_tt = tt_suite.run(train_td, test_td)
result_tt.save_as_html("deepchecks_train_test_validation.html")

print("✅ Reports generated: deepchecks_data_integrity.html, deepchecks_train_test_validation.html")
