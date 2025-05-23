# 📦 Backend - AI Prompt Generator

This is the backend service for the **AI Prompt Generator** web application. It handles user queries, generates AI-based responses using prompt engineering, and stores the interaction history in a PostgreSQL database.

More modularity, but I love separating files and clarity.
---

## Related Repos

* Frontend (Streamlit): [AI-Prompt-Frontend](https://unbeatablebann-ai-prompt-generator-app-vachgp.streamlit.app/)
* Frontend (Github): [AI-Prompt-Frontend-repo](https://github.com/UnbeatableBann/AI-Prompt-Generator)
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
  └── test_full.py          # Full integration flow test
  └── test_prompt.py        # Unit tests for prompt formatting
```

---

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/UnbeatableBann/AI-Prompt-Generator-Backend.git
cd AI-Prompt-Generator-Backend
```

### 2. Create and activate a virtual environment

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
Done with vibe coding, but expect this all is done by me. 👍

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
