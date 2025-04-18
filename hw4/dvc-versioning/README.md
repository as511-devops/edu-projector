# 📦 Install DVC (with optional S3 support if needed)
pip install "dvc[s3]"

# ✅ Initialize DVC inside a Git-tracked subdirectory
dvc init --subdir
git add .dvc .dvcignore
git commit -m "Initialize DVC in subdir"

# 🛑 Remove the data file from Git tracking (keep it on disk)
git rm -r --cached banking_support_500_ukr.csv
git commit -m "Stop tracking banking_support_500_ukr.csv (moving to DVC)"

# 📁 Track your data file with DVC
dvc add banking_support_500_ukr.csv

# 📝 Add .dvc file and .gitignore to Git
git add banking_support_500_ukr.csv.dvc .gitignore
git commit -m "Track banking_support_500_ukr.csv with DVC"

# ☁️ (Optional) Configure and push to DVC remote (like S3)
# dvc remote add -d myremote s3://your-bucket-name/path/to/dvc-store
# dvc remote modify myremote access_key_id <your-access-key>
# dvc remote modify myremote secret_access_key <your-secret-key>
# dvc push

# 🔀 Push everything to GitHub
git push origin <your-branch-name>
