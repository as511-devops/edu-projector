import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from cleanlab.classification import CleanLearning

df = pd.read_csv("banking_support_500_ukr.csv")
X_raw = df["text"].astype(str).tolist()
y_raw = df["category"].astype(str).tolist()

le = LabelEncoder()
y = le.fit_transform(y_raw)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X_raw)

clf = LogisticRegression(max_iter=1000)
clean_clf = CleanLearning(clf, seed=42)
clean_clf.fit(X=X, labels=y)

# Get all flagged indices, convert any to int, then take top 10
raw_issues = clean_clf.get_label_issues()
indices = []
for i in raw_issues:
    try:
        indices.append(int(i))
    except (ValueError, TypeError):
        continue
top_n = indices[:100]

print("\n⚠️ Top 10 potential label issues (index: text — original label):")
for idx in top_n:
    print(f"{idx}: {X_raw[idx]} — {y_raw[idx]}")
