import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold, cross_val_predict
from cleanlab.filter import find_label_issues

# Load normalized data
df = pd.read_csv("banking_support_500_ukr.csv")
X_raw = df["text"].astype(str).tolist()
y_raw = df["category"].astype(str).tolist()

# Encode labels
le = LabelEncoder()
y = le.fit_transform(y_raw)

# Vectorize text
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X_raw)

# Choose a text‑friendly classifier
clf = MultinomialNB()

# Get out‑of‑sample predicted probabilities with stratified CV
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
pred_probs = cross_val_predict(
    clf, X, y,
    cv=cv,
    method="predict_proba"
)

# Find and rank label issues
issues = find_label_issues(
    labels=y,
    pred_probs=pred_probs,
    return_indices_ranked_by="normalized_margin"
)

# Show the top 10 most suspicious
print("\n⚠️ Top 10 potential label issues:")
for idx in issues[:10]:
    print(f"{idx}: {X_raw[idx]} — {y_raw[idx]}")
