# MinIO CRUD Python Client

This repository contains a Python client for performing basic CRUD (Create, Read, Update, Delete) operations against a [MinIO](https://min.io/) S3-compatible object store.

## 🧱 Features

- ✅ Create and delete buckets
- ✅ Upload and download objects
- ✅ List objects in a bucket
- ✅ Delete objects
- ✅ Tested via `pytest` with local MinIO instance

---

## 🚀 Setup

### 1. Clone and Create Environment

```bash
git clone <repo-url>
cd minio-client
python3 -m venv .venv
source .venv/bin/activate

# To test
pytest
```
