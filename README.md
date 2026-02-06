# ai-cybersecurity-chatbot-rag
# 🛡️ AI Cybersecurity Chatbot – RAG-Based Security Assistant

Intelligent conversational assistant for cybersecurity support and malware education, powered by Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG).

This project was developed as part of my Cybersecurity Engineering thesis and focuses on automating technical support, improving response times, and providing secure, private, and offline AI-powered assistance for cybersecurity environments.

---

## 🚀 Overview

Security teams and users often require repetitive technical assistance related to malware, threats, and cybersecurity procedures. Manual support increases operational workload and response times.

This project introduces an **AI-driven chatbot** capable of:

- Answering cybersecurity questions
- Explaining malware behavior
- Providing technical guidance
- Querying an internal knowledge base
- Operating fully offline (privacy-preserving)

The system combines **semantic search + local LLM inference** to deliver accurate, contextual, and reliable responses.

---

## 🧠 Architecture

The assistant implements a **Retrieval-Augmented Generation (RAG)** pipeline:

User → Telegram Bot → Embeddings → Vector Search (ChromaDB) → LLM → Contextual Response

### Flow:

1. User sends a query via Telegram
2. Query is converted into embeddings
3. Semantic search retrieves relevant documents
4. Context is injected into the LLM
5. Model generates a precise answer

This approach improves accuracy and reduces hallucinations compared to standalone LLMs.

---

## ✨ Key Features

- 🤖 Telegram conversational interface
- 🧠 Local LLM execution (no cloud dependency)
- 🔎 Semantic search with embeddings
- 🗄️ Vector database using ChromaDB
- 📚 Custom cybersecurity knowledge base
- 🔒 Offline and privacy-preserving architecture
- ⚡ Automated technical support
- 📖 Malware education assistance

---

## 🛠 Tech Stack

### Core
- Python

### AI / NLP
- LLaMA (local LLM)
- HuggingFace Transformers
- SentenceTransformers (embeddings)
- Retrieval-Augmented Generation (RAG)

### Data
- ChromaDB (vector database)
- Pandas / NumPy

### Integration
- Telegram Bot API

### Environment
- Linux (Kali / Parrot)
- VirtualBox / VMware

---

## 📁 Project Structure
```
ai-cybersecurity-chatbot-rag/
│
├── src/
│   ├── bot.py
│   ├── config.py
│   ├── cortex_runner.py
│   ├── handlers.py
│   ├── knowledge_base.py
│   └── utils.py
│
├── data/
│   └── sample_knowledge_base.csv
│
├── docs/
│   └── architecture.png
│
├── requirements.txt
├── README.md
└── .gitignore
```
---
## Author
José Luis Sánchez Tamayo

