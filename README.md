# 📦 Backend - AI Prompt Generator

This is the backend service for the **AI Prompt Generator** web application. It handles user queries, generates AI-based responses using prompt engineering, and stores the interaction history in a PostgreSQL database.

---

## Related Repos

* Frontend (Streamlit): [AI-Prompt-Frontend](https://github.com/yourusername/ai-prompt-frontend)
---

## Features

* REST API built with Flask
* AI-generated responses using Gemini API
* Stores prompts and responses in PostgreSQL
* Supports user-based history management
* CORS enabled for frontend integration

---

## Tech Stack

* **Python**
* **Flask**
* **PostgreSQL**
* **SQLAlchemy**
* **dotenv**
* **Gemini/LLM Integration**

---

## Project Structure

```
backend/
├── app.py                  # Flask app with API routes
├── models.py               # SQLAlchemy models
├── ai_service.py             # DB session and engine config
├── .env                    # Environment variables (ignored)
├── .env.example            # Sample env config
├── requirements.txt        # Python dependencies
└── test/                   # Unit and integration tests
```

---

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/UnbeatableBann/ai-prompt-backend.git
cd ai-prompt-backend
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment

Create a `.env` file using the example:

```bash
cp .env.example .env
```

Update the `.env` with your:

* DATABASE\_URL
* GEMINI\_API\_KEY 

### 5. Start the server

```bash
flask run
```

---

## Testing

```bash
pytest
```

Includes:

* Unit tests for prompt formatting
* Mocked generation tests
* API route validation
* Full integration flow test

---

## API Endpoints

### `POST /generate`

Generate AI responses

```json
{
  "user_id": "user123",
  "query": "What is AI?",
  "tone": "casual"
}
```

### `GET /history?user_id=user123`

Get all previous interactions

---

## License

MIT

---

## Acknowledgements

Inspired by real-world use of prompt engineering in education and productivity tools.
