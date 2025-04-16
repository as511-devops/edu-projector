import uuid
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct, Distance, VectorParams, Filter

# Sample texts
texts = [
    "AI is transforming the world.",
    "Qdrant is a vector search engine.",
    "Vector databases are ideal for semantic search.",
    "Fast retrieval from millions of vectors.",
    "Sentence Transformers provide great embeddings."
]

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")
vectors = model.encode(texts).tolist()

# Connect to Qdrant
client = QdrantClient(host="localhost", port=6333)
collection_name = "pr7-demo"

# Create collection (if not exists)
if collection_name not in [col.name for col in client.get_collections().collections]:
    client.recreate_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(
            size=len(vectors[0]),
            distance=Distance.COSINE
        )
    )

# Clear all vectors (to have clean ran)
client.delete(
    collection_name=collection_name,
    points_selector=Filter(must=[])
)

# Upload vectors
points = [
    PointStruct(id=str(uuid.uuid4()), vector=vec, payload={"text": text})
    for vec, text in zip(vectors, texts)
]
client.upsert(collection_name=collection_name, points=points)

# Perform search
query = "semantic search engine"
query_vector = model.encode(query).tolist()

results = client.search(
    collection_name=collection_name,
    query_vector=query_vector,
    limit=3
)

print("🔍 Top search results:")
for hit in results:
    print(f"- {hit.payload['text']} (score={hit.score:.4f})")
