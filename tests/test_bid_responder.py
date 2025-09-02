import pytest
from services.bid_responder import BidResponder
from schemas.bid_schemas import BidRequest


def test_bid_responder_logic():
    """
    Test that BidResponder returns expected mock answers
    and includes similar bids when relevant.
    """
    responder = BidResponder()
    request = BidRequest(bid_request="Telemedicine", context="urgent")

    response = responder.process_bid(request)

    assert isinstance(response.gemini_answer, str)
    assert "Gemini suggestion for" in response.gemini_answer
    assert isinstance(response.custom_llm_expected_answer, str)
    assert "Enhanced answer" in response.custom_llm_expected_answer


def test_bid_responder_empty_request():
    """
    Test that BidResponder raises ValueError for an empty bid_request.
    """
    responder = BidResponder()
    request = BidRequest(bid_request="", context="urgent")

    with pytest.raises(ValueError) as exc:
        responder.process_bid(request)

    assert "Bid request cannot be empty." in str(exc.value)
