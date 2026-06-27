import chromadb
from chromadb.utils.embedding_functions.ollama_embedding_function import (
    OllamaEmbeddingFunction,
)

# Read the profile.txt file and split it into a list of lines   
with open('profile.txt', 'r') as file:
    file = file.read()
    file = file.split("\n")


# Create a list of tuples with the line and the index
file = [(line, index) for index, line in enumerate(file)]
# Save data to disk so it survives restarts
client = chromadb.PersistentClient(path="./chroma_db")

# Connect to Ollama's embedding model to convert text into vectors
ef = OllamaEmbeddingFunction(
    model_name="nomic-embed-text",
    url="http://localhost:11434",  # Ollama's default local address
)

# Create (or reuse) a collection - like a table in a database
collection = client.get_or_create_collection(
    name="personal_profile",
    embedding_function=ef,  # Tells ChromaDB how to convert text to vectors
)

for line, index in file:
    collection.add(
        documents=[line],
        metadatas=[{"source": "profile"}],
        ids=[str(index)],
    )
print("Data added to collection")
print(collection.count())



