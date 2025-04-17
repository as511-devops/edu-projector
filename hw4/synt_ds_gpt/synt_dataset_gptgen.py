import os
import json
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI
from openai import OpenAIError

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

prompt = """
Generate a synthetic dataset of 10 support chat messages.
Each message must include:
- message: a user support question
- category: one of [billing, technical, access, general]

Respond ONLY with raw JSON. Do NOT include markdown or explanation text.
"""

try:
    resp = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates data."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )
except OpenAIError as e:
    print("❌ OpenAI API error:", e)
    exit(1)

raw = resp.choices[0].message.content.strip()

try:
    data = json.loads(raw)
except json.JSONDecodeError:
    cleaned = raw.strip("`").split("```")[-1]
    data = json.loads(cleaned)

df = pd.DataFrame(data)
df.to_csv("synthetic_dataset.csv", index=False)
print("✅ Saved synthetic_dataset.csv")
