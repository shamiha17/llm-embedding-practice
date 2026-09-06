from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

texts = [
    "The cow has fever",
    "The cow is sick",
    "I like playing football"
]

embeddings = model.encode(texts)

similarity = cosine_similarity(embeddings)

print(similarity)