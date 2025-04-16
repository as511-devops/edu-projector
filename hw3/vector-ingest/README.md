## TL;DR
* Embeds a list of example texts
* Connects to your running Qdrant instance
* Creates a collection with cosine distance
* Uploads the vectors
* Executes a similarity search

## Output example
```bash
🔍 Top search results:
- Vector databases are ideal for semantic search. (score=0.6790)
- Qdrant is a vector search engine. (score=0.3874)
- Fast retrieval from millions of vectors. (score=0.3299)
```

## 🚀 Qdrant Kubernetes Deployment & Management

```bash
# 1️⃣ Add Qdrant Helm repository and install
helm repo add qdrant https://qdrant.to/helm
helm repo update
helm install qdrant qdrant/qdrant

# 2️⃣ Port-forward to access the API
kubectl port-forward svc/qdrant 6333:6333
# Access API: http://localhost:6333

# 3️⃣ Stop Qdrant (scale down StatefulSet, data is preserved)
kubectl scale statefulset qdrant --replicas=0

# 4️⃣ Start Qdrant again
kubectl scale statefulset qdrant --replicas=1

# 5️⃣ Restart Qdrant (graceful rollout)
kubectl rollout restart statefulset qdrant

# 6️⃣ Uninstall Qdrant but keep PVC
helm uninstall qdrant

# 7️⃣ (Optional): 
## Delete Qdrant PVC and all data
  kubectl delete pvc qdrant-storage-qdrant-0

## To forward Qdrant's ports execute one of the following commands:
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=qdrant,app.kubernetes.io/instance=qdrant" -o jsonpath="{.items[0].metadata.name}")

## If you want to use Qdrant via http execute the following commands
  kubectl --namespace default port-forward $POD_NAME 6333:6333

## If you want to use Qdrant via grpc execute the following commands
  kubectl --namespace default port-forward $POD_NAME 6334:6334

## If you want to use Qdrant via p2p execute the following commands
  kubectl --namespace default port-forward $POD_NAME 6335:6335

```
