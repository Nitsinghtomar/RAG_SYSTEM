
# 🤖 RAG System - Intelligent Document Q&A API

A robust **Retrieval-Augmented Generation (RAG) System** built with Flask that combines document ingestion, semantic search, and AI-powered response generation. This system allows you to upload documents, perform intelligent searches, and get contextually accurate answers powered by state-of-the-art language models.

## ✨ Key Capabilities

- **Smart Document Processing**: Automatically process and index PDF documents for semantic search
- **Vector-Based Retrieval**: Leverage Qdrant vector database for efficient similarity search
- **AI-Powered Generation**: Generate contextually relevant answers using advanced language models
- **Multiple Operation Modes**: Support for retrieval-only, generation, and comparative analysis modes
- **Scalable Architecture**: Clean, modular design with Flask blueprints for easy maintenance and extension
- **Production Ready**: Built with deployment and scalability in mind

## 🏗️ System Architecture

```
RAG_SYSTEM/
├── api/
│   ├── __init__.py               # API package initialization
│   ├── common.py                 # Shared utilities and configurations
│   ├── comparative_analysis.py   # Advanced analysis modes with custom prompts
│   ├── generation.py             # Response generation endpoints
│   ├── ingestion.py              # Document processing and indexing
│   └── retrieval.py              # Semantic search and retrieval
├── data/
│   └── [your-documents].pdf      # Document storage directory
├── config.py                     # Application configuration
├── app.py                        # Main Flask application
├── ingest_data.py                # Data ingestion utility script
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## 🚀 Getting Started

### 1. Repository Setup

```bash
git clone https://github.com/Nitsinghtomar/RAG_SYSTEM.git
cd RAG_SYSTEM
```

### 2. Environment Configuration

**Create Virtual Environment:**

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/macOS
```

**Install Dependencies:**

```bash
pip install -r requirements.txt
```

**Configure Environment Variables:**

Create a `.env` file in the project root:

```env
# Qdrant Vector Database Configuration
QDRANT_URL=your_qdrant_cloud_url
QDRANT_API_KEY=your_qdrant_api_key

# Language Model Configuration  
GROQ_API_KEY=your_groq_api_key

# Application Settings
DEBUG=True
```

### 3. Document Ingestion

Process your documents and create vector embeddings:

```bash
python ingest_data.py
```

### 4. Launch the Application

```bash
python app.py
```

The API will be available at `http://localhost:5000`

## 📋 API Reference

### Document Retrieval

**Endpoint:** `POST /api/retrieve`

Retrieve relevant document chunks based on semantic similarity.

```json
{
  "query": "What are the main topics covered in the document?"
}
```

### AI-Powered Response Generation

**Endpoint:** `POST /api/generate`

Generate comprehensive answers using retrieved context.

```json
{
  "mode": "generation",
  "query": "Explain the key concepts discussed in the document"
}
```

### Advanced Analysis Modes

**Endpoint:** `POST /api/query`

Multi-mode endpoint supporting different analysis types:

```json
{
  "mode": "comparative",  // Options: "retrieval", "generation", "comparative"
  "query": "Compare different approaches mentioned in the document"
}
```

## 🛠️ Technology Stack

- **Backend Framework**: Flask with Blueprint architecture
- **Vector Database**: Qdrant Cloud for semantic search
- **Language Models**: Groq API integration (LLaMA 3)
- **Document Processing**: LangChain with PyPDF
- **Embeddings**: FastEmbed for efficient vector generation

## 🔧 Configuration Options

The system can be customized through `config.py`:

- **Model Selection**: Switch between different language models
- **Collection Settings**: Configure vector database collections
- **Embedding Models**: Adjust embedding model parameters
- **Debug Settings**: Control application logging and debugging

## 🤝 Contributing

We welcome contributions! Feel free to:

- Submit bug reports and feature requests
- Create pull requests for improvements
- Share feedback and suggestions

## 📄 License

This project is open source and available under the MIT License.

---

**Built with ❤️ for intelligent document processing and AI-powered Q&A systems**