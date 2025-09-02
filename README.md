# healthcare-bid-service

# AI-Powered Healthcare Bidding Microservice

A production-ready **FastAPI microservice** that processes healthcare bid requests, simulates AI-generated responses, and applies a custom enhancement layer.  
Includes a **mock Retrieval-Augmented Generation (RAG)** system, a **React frontend**, unit tests, and Docker support.

---

## 🚀 Features

- **FastAPI Backend** with `/bid-response` POST endpoint.
- **Gemini AI Simulation**: Generates a mock AI response.
- **Custom LLM Enhancement**: Improves the base AI response with context or scoring logic.
- **Retrieval-Augmented Generation (RAG)**: Returns top-k similar past bids (mock embeddings).
- **Modular Architecture**: Clean separation of routes, services, schemas, and retrieval logic.
- **React Frontend**: Simple UI to submit bids and view responses.
- **Unit Tests**: Tests for API endpoint and service logic.
- **Dockerfile**: Multi-stage, production-ready container setup.

---

## 🗂️ Project Structure

healthcare-bid-service/
├── Dockerfile
├── README.md
├── requirements.txt
├── main.py
├── routes/
│ └── bid_routes.py
├── services/
│ └── bid_responder.py
├── schemas/
│ └── bid_schemas.py
├── retrieval/
│ └── retriever.py
├── tests/
│ ├── test_api.py
│ └── test_bid_responder.py
└── frontend/
└── React app for submitting bids

---

## 🛠️ Setup Instructions

### 1. Clone Repository

```bash
git clone <your-repo-url>
cd healthcare-bid-service

### 2. Backend Setup (Local)
Create a virtual environment and install dependencies:

python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows

pip install -r requirements.txt

uvicorn main:app --reload

Backend will run at: http://localhost:8000
Docs: http://localhost:8000/docs

### Frontend Setup (Local)

cd frontend
npm install
npm start

Frontend will run at: http://localhost:3000

### Docker Setup (Pending Network Fix)

docker build -t healthcare-bid-service .
docker run -p 8000:8000 healthcare-bid-service

### 🧪 Run Tests
pytest -v

## API Example

Request
POST /bid-response/
{
  "bid_request": "Need telemedicine services",
  "context": "Urgent, rural area"
}
Response
{
  "gemini_answer": "Gemini suggestion for: Need telemedicine services",
  "custom_llm_expected_answer": "Enhanced answer using context: Urgent, rural area. Similar past bids: Telemedicine consultation package"
}
```

## Architecture Overview

This project demonstrates a production-ready AI microservice design:
FastAPI Backend: Clean separation of concerns with modular folders:
routes/: API endpoints
services/: Core business logic
schemas/: Pydantic request/response models
retrieval/: Mock RAG implementation
AI Simulation: Placeholder Gemini answer generator and mock enhancement layer.
RAG Integration: Simulated vector search with cosine similarity (no real embeddings required).
React Frontend: Simple UI for testing endpoints.
Docker: Multi-stage build for lightweight container deployment.
This approach prioritizes clarity, extensibility, and production readiness.
