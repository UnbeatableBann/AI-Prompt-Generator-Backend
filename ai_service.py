import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Set up 
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

def call_gemini(prompt):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    print(response.text)
    return response.text.strip()

def refine(prompt):
    polish = f"Polish and refine the following explanation for clarity:\n\n{prompt}"
    print(f"Polishing prompt: {polish}")
    return call_gemini(polish)

def generate_casual(query):
    initial = f"Explain this casually and in a friendly tone:\n{query}"
    casual_draft = call_gemini(initial)
    polished = refine(casual_draft)
    return polished

def generate_formal(query):
    initial = f"Provide an academic and analytical explanation of:\n{query}"
    formal_draft = call_gemini(initial)
    polished = refine(formal_draft)
    return polished
