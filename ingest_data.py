"""
Data Ingestion Script for RAG System
This script processes documents in the 'data' folder and creates vector embeddings
that are stored in Qdrant vector database for semantic search capabilities.

Usage:
    python ingest_data.py

Prerequisites:
    - Documents placed in the 'data' folder
    - Qdrant database configured in .env file
    - Required dependencies installed
"""

from api.ingestion import ingest

if __name__ == "__main__":
    print("Starting document ingestion process...")
    retriever = ingest()
    print("✅ Data ingested successfully into Qdrant vector database.")
    print("🚀 Your RAG system is ready to use!")
