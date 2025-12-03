# 🌐 Enterprise Assistant — AI-Powered RAG System for Enterprise Knowledge Retrieval
A full-stack Retrieval-Augmented Generation (RAG)–based enterprise assistant designed to help organizations retrieve information from policies, HR manuals, SOPs, compliance docs, legal documents, and corporate emails — using natural language queries.

This project brings together:
⚛️ React.js — Frontend
🚀 Express.js (Node.js) — Backend API
🧠 FastAPI + FAISS + LLM (Gemini/OpenAI) — RAG Pipeline
🗂️ Company-wise Multi-Index Architecture — Secure, scalable document retrieval

---

## 📌 Table of Contents

- [Screenshots/UI](#screenshots-ui)
- [Overview](#overview)
- [Key Features](#key-features)
- [System Architechture](#system-architechture)
- [RAG Workflow](#rag-workflow)
- [Tech Stack](#tech-stack)

---
## Screenshots/UI

Admin Dashboard

<img width="1600" height="1208" alt="screen" src="https://github.com/user-attachments/assets/7f0bb42e-5b5b-45c1-9d88-44bc2cce7b28" />

ChatBot Interface

<img width="1600" height="1000" alt="screen" src="https://github.com/user-attachments/assets/f03bfcb3-ccb2-460f-89f9-0fc503e52d7e" />





## 🔎 Overview

Enterprise Assistant is an intelligent system that enables employees to search internal documents using simple natural language questions.

Instead of manually reading long policy PDFs, users simply ask:

“What is the maternity leave policy?”
“What is the onboarding process for new employees?”
“What is the reimbursement limit for travel?”

✨ The system retrieves the relevant text chunks using FAISS and generates a grounded answer using an LLM.

## ⭐ Key Features
- 📄 Upload PDFs & Documents through a clean UI
- 🧩 Semantic Chunking for better context retrieval
- 🧠 RAG Pipeline with FAISS retrieval + LLM answer generation
- 🏢 Company-wise isolated indexes
- 🔐 Role-based access (Admin & Employee)
- 💬 Chat-style interface for querying enterprise documents
- ⚙️ Modular ML pipeline (swap embedding/LLM models easily)
- 📈 Scalable microservice architecture
## 🏗️ System Architecture
<img width="789" height="242" alt="image" src="https://github.com/user-attachments/assets/09ffe94b-d028-4b66-a440-6aa1178fcbe9" />

## 🔄 RAG Workflow
<img width="338" height="461" alt="image" src="https://github.com/user-attachments/assets/24212e1c-86f4-42f8-9bb4-66e59dc69e2c" />

## 🛠️ Tech Stack
### Frontend

- ⚛️ React.js
- TailwindCSS
- Axios

### Backend

- 🚀 Node.js
- Express.js
- Multer (file uploads)
- JWT Authentication

### ML Service

- 🧠 FastAPI
- FAISS Vector Store
- LLM (Gemini/OpenAI)
- LangChain components
