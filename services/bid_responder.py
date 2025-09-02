from schemas.bid_schemas import BidRequest, BidResponse
from retrieval.retriever import Retriever


class BidResponder:
    """
    Handles AI bidding logic:
    - Simulates a base Gemini answer
    - Applies a custom enhancement layer
    - Integrates Retrieval-Augmented Generation (RAG)
    """

    def __init__(self) -> None:
        self.retriever = Retriever()

    def process_bid(self, request: BidRequest) -> BidResponse:
        """
        Process a bid request and return a response.

        Args:
            request (BidRequest): Incoming bid request containing bid text and optional context.

        Returns:
            BidResponse: Contains a Gemini mock answer and enhanced answer.

        Raises:
            ValueError: If bid_request is empty or invalid.
        """
        try:
            if not request.bid_request.strip():
                raise ValueError("Bid request cannot be empty.")

            # Mock Gemini AI answer
            gemini_answer = f"Gemini suggestion for: {request.bid_request}"

            # Custom LLM enhancement
            custom_answer = (
                f"Enhanced answer using context: {request.context or 'No context provided'}"
            )

            # Retrieve similar bids (mock RAG)
            similar_bids = self.retriever.find_similar_bids(request.bid_request)
            if similar_bids:
                custom_answer += f". Similar past bids: {', '.join(similar_bids)}"

            return BidResponse(
                gemini_answer=gemini_answer,
                custom_llm_expected_answer=custom_answer,
            )

        except Exception as e:
            print(f"Error in BidResponder.process_bid: {str(e)}")
            raise
