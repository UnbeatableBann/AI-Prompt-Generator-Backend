from flask import Flask, request, jsonify
from flask_cors import CORS
from models import Base, Prompt, SessionLocal, engine
from ai_service import generate_casual, generate_formal
from datetime import datetime

Base.metadata.create_all(bind=engine)
app = Flask(__name__)
CORS(app)

@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.json
        print(f"Received data: {data}")
        user_id = data.get("user_id")
        query = data.get("query")
        tone = data.get("tone")

        if not user_id or not query:
            return jsonify({"error": "Missing user_id or query"}), 400

        casual = None
        formal = None

        if tone == "casual":
            casual = generate_casual(query)
            formal = None
        elif tone == "formal":
            casual = None   
            formal = generate_formal(query)
        else:
            casual = generate_casual(query)
            formal = generate_formal(query)

        session = SessionLocal()
        prompt = Prompt(
            user_id=user_id,
            query=query,
            casual_response=casual,
            formal_response=formal,
            created_at=datetime.utcnow()
        )
        session.add(prompt)
        session.commit()
        session.close()

        return jsonify({
            "casual_response": casual or "",
            "formal_response": formal or ""
        })
    except Exception as e:
        print(f"Error in /generate: {e}")
        return jsonify({"error": "Internal server error"}), 500


@app.route("/history")
def history():
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"error": "Missing user_id"}), 400
    session = SessionLocal()
    prompts = session.query(Prompt).filter_by(user_id=user_id).order_by(Prompt.created_at.desc()).all()
    session.close()

    history = [{
        "query": p.query,
        "casual_response": p.casual_response,
        "formal_response": p.formal_response,
        "created_at": p.created_at.isoformat()
    } for p in prompts]

    return jsonify(history)

if __name__ == "__main__":
    app.run(debug=True)
