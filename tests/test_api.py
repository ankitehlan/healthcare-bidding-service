from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_post_bid_response():
    """
    Test that the /bid-response endpoint returns
    valid Gemini and custom answers for valid input.
    """
    payload = {"bid_request": "Telemedicine", "context": "urgent"}
    response = client.post("/bid-response/", json=payload)

    # Status code check
    assert response.status_code == 200

    data = response.json()

    # Validate keys and types
    assert "gemini_answer" in data
    assert "custom_llm_expected_answer" in data
    assert isinstance(data["gemini_answer"], str)
    assert isinstance(data["custom_llm_expected_answer"], str)


def test_post_bid_response_empty_request():
    """
    Test that an empty bid_request triggers a 400 Bad Request error.
    """
    payload = {"bid_request": "", "context": "urgent"}
    response = client.post("/bid-response/", json=payload)

    # Status code should indicate validation error
    assert response.status_code == 400

    data = response.json()
    assert data["detail"] == "Bid request cannot be empty."
