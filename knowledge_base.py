import chromadb
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from config import CHROMA_DB_PATH, CSV_TRAIN_FILE, EMBEDDING_MODEL_NAME, EMBEDDING_DISTANCE_THRESHOLD

client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
embedder = SentenceTransformer(EMBEDDING_MODEL_NAME)

try:
    collection = client.get_collection(name="qna_collection")
except:
    collection = client.create_collection(name="qna_collection")
    df = pd.read_csv(CSV_TRAIN_FILE)
    questions, answers = df['Pregunta'].tolist(), df['Respuesta'].tolist()
    embeddings = embedder.encode(questions, convert_to_tensor=True)
    ids = [f"doc_{i}" for i in range(len(questions))]

    for i, embedding in enumerate(embeddings):
        collection.add(
            documents=[questions[i]],
            metadatas=[{"respuesta": answers[i]}],
            embeddings=[embedding.numpy()],
            ids=[ids[i]]
        )

def obtener_respuesta_semantica(pregunta_usuario):
    query_embedding = embedder.encode([pregunta_usuario], convert_to_numpy=True)
    results = collection.query(query_embeddings=query_embedding, n_results=2)

    if results.get("distances"):
        distancia = results["distances"][0][0]
        if distancia <= EMBEDDING_DISTANCE_THRESHOLD and results.get("metadatas"):
            return results["metadatas"][0][0]["respuesta"]
    return None