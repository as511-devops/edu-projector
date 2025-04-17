## 🚀 Label Studio Deployment on Kubernetes

To deploy Label Studio on Kubernetes and access it locally:

```bash
# 2️⃣ Apply the Kubernetes resources (Deployment, Service, PVC, Namespace)
kubectl apply -f label-studio.yaml

# 3️⃣ Forward port to access Label Studio in your browser
kubectl port-forward -n label-studio svc/label-studio 8080:8080
# Then open http://localhost:8080 in your browser

# 4️⃣ To clean up everything if needed
kubectl delete ns label-studio
```

## 🚀 Label Studio Deployment on Docker
# 📦 Create persistent volume
docker volume create labelstudio_data

# 🚀 Run Label Studio container with persistent volume
docker run -d \
  --name label-studio \
  -p 8080:8080 \
  -v labelstudio_data:/label-studio/data \
  heartexlabs/label-studio:latest

# 🌐 Access Label Studio in your browser
# Visit: http://localhost:8080

# 🧹 Cleanup instructions
# Stop and remove the container
docker stop label-studio && docker rm label-studio

# (Optional) Remove the persistent volume
docker volume rm labelstudio_data
