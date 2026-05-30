# Multi Agent System – RAG & Document Review Platform

## Project Description

Academic Agent System is an AI-powered document intelligence platform designed to analyze academic and technical PDF documents using Retrieval-Augmented Generation (RAG).

The system allows users to upload PDF files, extract and preprocess document text, generate semantic embeddings, store them in a vector database, and interact with the document through natural language questions.

In addition to question answering, the project also includes a technical review module that analyzes uploaded content for:

* Unsupported claims
* Missing assumptions
* Weak evidence
* Overgeneralization

The application combines FastAPI, Streamlit, SentenceTransformers, ChromaDB, and Google Gemini to create a modular multi-agent workflow for intelligent document analysis.

---
## Overview

The Academic Agent System is a modular AI-based document analysis platform built using a Retrieval-Augmented Generation (RAG) architecture.

Users can:

* Upload academic or technical PDF documents
* Ask questions based strictly on uploaded content
* Retrieve semantically relevant document chunks
* Generate AI-assisted answers
* Produce structured technical review reports

The project demonstrates concepts from:

* NLP
* Semantic Search
* Embeddings
* Vector Databases
* Retrieval-Augmented Generation (RAG)
* Multi-agent AI workflows
* Backend API development

---

## Features

### PDF Upload & Processing

* Upload PDF documents using the Streamlit interface
* Extract text using `pypdf`
* Split text into semantic chunks
* Clean noisy or irrelevant chunks

### Embedding Generation

* Generate embeddings using:

  * `SentenceTransformer`
  * `all-MiniLM-L6-v2`

### Persistent Vector Storage

* Store embeddings and chunks using ChromaDB
* Persistent storage survives backend restarts

### Retrieval-Augmented Question Answering

* Query rewriting for better semantic retrieval
* Context retrieval from vector database
* Gemini-based answer generation
* Responses constrained strictly to uploaded document context

### Technical Review Module

Generates a structured review report containing:

* Unsupported claims
* Missing assumptions
* Weak evidence
* Overgeneralization
* Overall risk score

### Streamlit Frontend

Interactive interface with:

* Sidebar PDF upload
* Question-answering tab
* Technical review analysis tab

---

# System Architecture

```text
PDF Upload
     ↓
PDF Text Extraction
     ↓
Text Chunking & Cleaning
     ↓
Embedding Generation
     ↓
ChromaDB Vector Storage
     ↓
Semantic Retrieval
     ↓
Gemini Response Generation
     ↓
Answer / Review Report
```

---

# Project Structure

```text
academic-agent-system/
│
├── backend/
│   ├── agents/
│   │   ├── filtering_agent.py
│   │   ├── query_agent.py
│   │   ├── reasoning_agent.py
│   │   ├── retrieval_agent.py
│   │   ├── review_agent.py
│   │   └── verifier_agent.py
│   │
│   ├── routers/
│   │   ├── upload.py
│   │   ├── query.py
│   │   ├── summarize.py
│   │   └── review.py
│   │
│   ├── services/
│   │   ├── embeddings.py
│   │   ├── vectorstore.py
│   │   └── llm.py
│   │
│   ├── utils/
│   │   ├── chunking.py
│   │   └── pdf_parser.py
│   │
│   └── main.py
│
├── frontend/
│   └── app.py
│
├── chroma_db/
│
└── venv/
```

---

# Technologies Used

## Backend

* FastAPI
* Python
* REST APIs

## Frontend

* Streamlit

## AI / NLP

* Google Gemini API
* SentenceTransformers
* all-MiniLM-L6-v2

## Vector Database

* ChromaDB

## PDF Processing

* pypdf

## Utilities

* python-dotenv
* requests

---

# Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/academic-agent-system.git
cd academic-agent-system
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## 5. Run FastAPI Backend

```bash
uvicorn backend.main:app --reload
```

Backend runs on:

```text
http://localhost:8000
```

---

## 6. Run Streamlit Frontend

```bash
streamlit run frontend/app.py
```

---

# API Endpoints

## Upload PDF

```http
POST /upload
```

Uploads and processes PDF documents.

---

## Ask Questions

```http
POST /ask
```

Query Parameters:

```text
question=<your_question>
```

Returns AI-generated answers using RAG.

---

## Generate Review Report

```http
POST /review
```

Generates a technical review report from uploaded content.

---

# Example Workflow

1. Upload a PDF document
2. System extracts and chunks text
3. Embeddings are generated
4. Chunks stored in ChromaDB
5. User asks a question
6. Relevant chunks retrieved semantically
7. Gemini generates a context-aware response
8. User can additionally generate a technical review report

---

# Current Progress

## Completed

* PDF parsing
* Chunking pipeline
* Embedding generation
* Vector database integration
* RAG-based Q&A
* Technical review module
* Streamlit UI
* FastAPI integration

## In Progress

* Summarization module
* Improved retrieval filtering
* Better context validation
* Enhanced error handling
* Deployment optimization

---

# Challenges Faced

## 1. Noisy PDF Extraction

Some PDFs contained metadata, broken text, or unwanted fragments.

### Solution

Implemented chunk cleaning and filtering logic.

---

## 2. Retrieval Relevance

Initial retrieval sometimes returned broad or weak context.

### Solution

Added semantic query rewriting before retrieval.

---

## 3. Context Length Management

Large documents could exceed LLM context limitations.

### Solution

Restricted retrieved context and optimized chunk handling.

---

# Future Improvements

* Multi-document support
* Citation-aware answers
* OCR support for scanned PDFs
* Authentication system
* Advanced summarization pipeline
* Hybrid retrieval (BM25 + embeddings)
* Docker deployment
* Cloud deployment
* Agent orchestration improvements

---

# Learning Outcomes

This project helped strengthen understanding of:

* Retrieval-Augmented Generation (RAG)
* Vector databases
* Embedding pipelines
* AI agent workflows
* Backend API architecture
* Semantic search systems
* LLM integration
* Modular software design

