# MinIO Deployment Guide

This guide explains how to deploy [MinIO](https://min.io/) in three different environments:
- ✅ Locally (binary)
- ✅ Docker
- ✅ Kubernetes

---

## ⚙️  1. Deploy MinIO Locally (Binary)
### 📥 Download MinIO
```bash
wget https://dl.min.io/server/minio/release/linux-amd64/minio
chmod +x minio
sudo mv minio /usr/local/bin/
```
### 🚀 Run MinIO 
```bash
mkdir -p ~/minio-data

MINIO_ROOT_USER=admin \
MINIO_ROOT_PASSWORD=admin123 \
minio server ~/minio-data --console-address ":9001"
```

## 🐳 2. Deploy MinIO using Docker
### 🐋 Pull and Run Container
```bash
docker run -d -p 9000:9000 -p 9001:9001 \
  --name minio \
  -e "MINIO_ROOT_USER=admin" \
  -e "MINIO_ROOT_PASSWORD=admin123" \
  -v ~/minio-docker-data:/data \
  quay.io/minio/minio server /data --console-address ":9001"
```
### 🔗 Access
MinIO API: http://localhost:9000
MinIO Console: http://localhost:9001

## ☸️  3. Deploy MinIO in K8s
### 📥 Option A. Manual k8s way
```bash
# Create a local cluster using kind (if needed)
kind create cluster --name minio-cluster

# Create a namespace for MinIO
kubectl create namespace minio

# Apply the MinIO standalone YAML manifest
kubectl apply -n minio -f https://raw.githubusercontent.com/minio/minio/master/docs/orchestration/kubernetes/minio-standalone.yaml

# (Optional) Expose MinIO service via NodePort
kubectl expose pod minio \
  --port=9000 --target-port=9000 --type=NodePort -n minio

# Wait until the pod is ready
kubectl get pods -n minio -w

# Get MinIO NodePort and access credentials
kubectl get svc -n minio
kubectl logs -n minio pod/minio

# (Optional) Port-forward to localhost
kubectl port-forward svc/minio 9000:9000 -n minio

# Access MinIO Web Console at:
# http://localhost:9000
```
### 🧪 Option B. Apply K8s local deployment
```bash
# checkout repo
cd <repo_locatio>/hw3/
kubectl create namespace minio
kubectl apply -f minio-deployment.yaml
kubectl apply -f minio-service.yaml
kubectl port-forward svc/minio 9001:9001 -n minio
# OR to send to background 
nohup kubectl port-forward svc/minio 9001:9001 -n minio > minio-forward.log 2>&1 &
``` 
Then access:
 🔐 API: http://localhost:9000
 🌐 Web UI: http://localhost:9001
Login: admin / admin123
