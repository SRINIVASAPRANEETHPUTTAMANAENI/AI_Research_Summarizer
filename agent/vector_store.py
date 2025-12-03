import faiss
from .hf_llm import HFEmbeddings

def create_vector_store(texts=None):
    texts = texts or ["dummy initialization text"]
    embeddings_model = HFEmbeddings()
    vectors = embeddings_model.embed_documents(texts)
    
    dim = vectors.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(vectors)
    
    store = {"index": index, "texts": texts, "embeddings_model": embeddings_model}
    return store

def add_to_store(store, texts):
    vectors = store['embeddings_model'].embed_documents(texts)
    store['index'].add(vectors)
    store['texts'].extend(texts)
