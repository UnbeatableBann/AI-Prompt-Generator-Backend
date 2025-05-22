from unittest.mock import patch, MagicMock
from backend.ai_service import generate_casual, generate_formal, call_gemini

@patch("backend.ai_service.call_gemini")
def test_generate_casual(mock_call):
    mock_call.side_effect = [
        "This is a rough casual version.",
        "This is a polished casual version."
    ]
    query = "What is machine learning?"
    result = generate_casual(query)

    assert "polished casual" in result
    assert mock_call.call_count == 2
    mock_call.assert_any_call("Explain this casually and in a friendly tone:\nWhat is machine learning?")
    mock_call.assert_any_call("Polish and refine the following explanation for clarity:\n\nThis is a rough casual version.")

@patch("backend.ai_service.call_gemini")
def test_generate_formal(mock_call):
    mock_call.side_effect = [
        "This is a rough formal version.",
        "This is a polished formal version."
    ]
    query = "Explain quantum computing."
    result = generate_formal(query)

    assert "polished formal" in result
    assert mock_call.call_count == 2
    mock_call.assert_any_call("Provide an academic and analytical explanation of:\nExplain quantum computing.")
    mock_call.assert_any_call("Polish and refine the following explanation for clarity:\n\nThis is a rough formal version.")

@patch("backend.ai_service.client")
def test_call_gemini(mock_client):
    mock_response = MagicMock()
    mock_response.text = "This is Gemini's response."

    mock_model = MagicMock()
    mock_model.generate_content.return_value = mock_response
    mock_client.models = mock_model

    result = call_gemini("Test prompt")
    assert result == "This is Gemini's response."
