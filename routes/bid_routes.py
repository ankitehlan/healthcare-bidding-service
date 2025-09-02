from fastapi import APIRouter, HTTPException
from schemas.bid_schemas import BidRequest, BidResponse
from services.bid_responder import BidResponder

router = APIRouter()
responder = BidResponder()

@router.post("/", response_model=BidResponse)
def get_bid_response(request: BidRequest) -> BidResponse:
    """
    Handle bid requests and return AI-simulated responses with RAG.

    Args:
        request (BidRequest): Request model containing bid and context.

    Returns:
        BidResponse: AI response and enhanced answer.
    """
    try:
        return responder.process_bid(request)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception:
        raise HTTPException(status_code=500, detail="Internal Server Error")
