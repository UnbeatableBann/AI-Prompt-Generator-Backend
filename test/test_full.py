import pytest
from unittest.mock import patch
from backend.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@patch('backend.ai_service.call_gemini')
def test_full_flow(mock_call_gemini, client):
    mock_call_gemini.side_effect = [
        "Casual response mock draft",
        "Casual response mock",
        "Formal response mock draft",
        "Formal response mock"
    ]
    response = client.post('/generate', json={
        "user_id": "testuser",
        "query": "test query",
        "tone": "both"
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["casual_response"] == "Casual response mock"
    assert data["formal_response"] == "Formal response mock"
    history_resp = client.get('/history', query_string={"user_id": "testuser"})
    assert history_resp.status_code == 200
    history_data = history_resp.get_json()
    assert len(history_data) > 0
    assert history_data[0]["casual_response"] == "Casual response mock"
    assert history_data[0]["formal_response"] == "Formal response mock"
