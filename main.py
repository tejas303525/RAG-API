from fastapi import FastAPI
import uvicorn
from typing import Optional
import chromadb
import ollama
from chromadb.utils.embedding_functions.ollama_embedding_function import (
    OllamaEmbeddingFunction,
)
from typing import List
from pydantic import BaseModel  # Pydantic is a library for data validation and parsing
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

app=FastAPI()
ollama_client = ollama.Client()
# Define the expected shape of incoming data for the POST endpoint
class DocumentSubmission(BaseModel):
    user_name: str  # Who this profile belongs to
    content: str  # The profile text to store

@app.post("/documents")  # POST endpoint - accepts data in the request body
def add_document(submission: DocumentSubmission):
    # Split the submitted profile into chunks by paragraph
    chunks = [chunk.strip() for chunk in submission.content.split("\n\n") if chunk.strip()]

    # Store each chunk in ChromaDB with the user's name attached as metadata
    collection.add(
        ids=[f"{submission.user_name}-chunk{i}" for i in range(len(chunks))],
        documents=chunks,
        metadatas=[
            {"source": "profile", "user_name": submission.user_name, "chunk_index": i}
            for i in range(len(chunks))  # user_name metadata lets us filter by user later
        ],
    )

    return {
        "message": f"Added {len(chunks)} chunks for user '{submission.user_name}'.",
        "user_name": submission.user_name,
        "chunks_added": len(chunks),
    }

@app.get("/ask")  # This creates a GET endpoint at /ask
def ask(question: str, user: Optional[str] = None):  # FastAPI reads "question" from the URL query string
    query_params={"query_texts": [question], "n_results": 2}

    if user:
        query_params["where"] = {"user_name": user}
    # RETRIEVE - find the 2 most relevant chunks from your knowledge base
    results = collection.query(**query_params)
    # Combine the matching chunks into a single string
    context = "\n\n".join(results["documents"][0])

    # AUGMENT - build a prompt that includes the retrieved context
    augmented_prompt = f"""Use the following context to answer the question.
                        If the context doesn't contain relevant information, say so.
                        Context:
                        {context}
                        Question: {question}
                        """

    # GENERATE - send the augmented prompt to the local LLM
    response = ollama_client.chat(
        model="qwen2.5:0.5b",
        messages=[{"role": "user", "content": augmented_prompt}],
    )

    # Return the answer along with the context so users can verify the source
    return {
        "question": question,
        "answer": response["message"]["content"],
        "context_used": results["documents"][0],
        "filtered_user_name": user,
    }




if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)