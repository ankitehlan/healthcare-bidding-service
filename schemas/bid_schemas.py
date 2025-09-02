from pydantic import BaseModel
from typing import Optional


class BidRequest(BaseModel):
    """
    Request schema for bid submissions.
    """
    bid_request: str
    context: Optional[str] = None


class BidResponse(BaseModel):
    """
    Response schema containing Gemini and custom answers.
    """
    gemini_answer: str
    custom_llm_expected_answer: str
