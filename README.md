# 📄 LegalPulse AI – Contract & Document Review Bot

![Frontend](https://img.shields.io/badge/Frontend-React%20%2B%20Tailwind-blue)
![Backend](https://img.shields.io/badge/Backend-FastAPI-green)
![LLM](https://img.shields.io/badge/LLM-Gemini%201.5%20Flash-orange)
![Deployment](https://img.shields.io/badge/Deployment-Vercel%20%2B%20Render-black)
![License](https://img.shields.io/badge/License-MIT-lightgrey)
![Status](https://img.shields.io/badge/Status-Live-success)

AI-powered contract analysis system that extracts key clauses, identifies risks, and generates plain-English summaries from legal documents.


## 🌐 Live Deployment

**Frontend (React + Tailwind):**  
👉 Live demo: https://legalpulse-ai.vercel.app/ Github repository: https://github.com/VaishnaviBasukar20/LegalPulse-AI-Frontend

**Backend (FastAPI + Gemini API):**  
👉 https://legalpulse-ai-backend.onrender.com/

**Backend API Docs (Swagger UI):**  
👉 https://legalpulse-ai-backend.onrender.com/docs


## 🧠 Overview

LegalPulse AI automates contract review by analyzing uploaded legal documents (PDF or raw text) and returning a structured, easy-to-understand report.

The system extracts:

- Key parties involved  
- Contract duration  
- Renewal terms  
- Payment terms  
- Termination clauses  
- Confidentiality provisions  
- Liability clauses  
- Intellectual property ownership  
- Risk indicators  
- Plain-English summary  


## 🚩 Risk Detection System

The system identifies and categorizes risks including:

- **Auto-renewal traps**
- **Liability exposure**
- **Missing exit clauses**
- **Indemnity risks**
- **IP ownership concerns**
- Other unusual or high-risk clauses

Each risk includes:

- Severity level (`Low`, `Medium`, `High`)
- Clear explanation of why it matters


## 🏗️ System Architecture

```bash
User
  ↓
React + Tailwind (Vercel)
  ↓
FastAPI Backend (Render)
  ↓
Gemini LLM API
```

## 🛠️ Tech Stack

### Frontend
- React
- Tailwind CSS
- Fetch API
- Vercel Deployment

### Backend
- FastAPI
- Pydantic (Strict Response Validation)
- PyMuPDF (PDF Parsing)
- Google Gemini API (`google-genai`)
- Render Deployment

## 🔄 Application Flow

1. User uploads a PDF or pastes contract text.
2. Backend extracts raw text from document.
3. Contract text is sent to Gemini API with structured instructions.
4. LLM returns structured JSON.
5. Pydantic validates the response schema.
6. Frontend displays organized report with highlighted risks.


## 📦 Backend Setup (Local Development)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/VaishnaviBasukar20/LegalPulse-AI-Backend.git
cd LegalPulse-AI-Backend
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
# or
source venv/bin/activate  # Mac/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Create .env File

```bash
GEMINI_API_KEY=your_api_key_here
```

### 5️⃣ Run Server

```bash
uvicorn main:app --reload
```

Access locally:

```bash
http://localhost:8000/docs
```

## 📦 Frontend Setup (Local Development)

Check [frontend repository](https://github.com/VaishnaviBasukar20/LegalPulse-AI-Frontend), for setup. Make sure your frontend url is added in the backend `CORS`. Update it in `main.py`.

## 🔐 Environment Variables - Backend

```bash
GEMINI_API_KEY=your_api_key_here
```

## 📊 Evaluation Coverage

| Requirement               | Status                      |
|---------------------------|-----------------------------|
| LLM API Integration       | ✅ Gemini API Integrated    |
| PDF/Text Input            | ✅ Supported                |
| Structured Output         | ✅ Pydantic Enforced        |
| Risk Flags                | ✅ Severity-Based           |
| Plain English Summary     | ✅ Implemented              |
| Clean UI                  | ✅ React + Tailwind         |
| Deployment                | ✅ Vercel + Render          |


## ⚠️ Notes

- Render free tier may enter sleep mode after inactivity. The first request may take 20–40 seconds.
- LLM output is strictly validated using Pydantic schema.
- If validation fails, the API returns structured error responses.

## 🚀 Future Improvements

- Clause highlighting inside original contract text  
- Downloadable PDF analysis report  
- Clause-level confidence scoring  
- Multi-language contract support  
- User authentication & document history  
- Vector search for contract clause comparison  
