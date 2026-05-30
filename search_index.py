from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
model=SentenceTransformer("all-miniLM-L6-v2")
videos=[
    "video about cooking pasta"
    "video about playing cricket"
    "video about eating habits"
]
encodings=model.encode(videos)
index=faiss.IndexFlatL2(len(encodings[0]))
index.add(np.array(encodings).astype('float32'))
query="eating tutorials"
def Search_videos(query,k=2):
    query_encoding=model.encode([query])
    D,I=index.search(
        np.array(query_encoding).astype('float32'),
        k=k
    )
    results=[videos[i] for i in I[0]]
    return results