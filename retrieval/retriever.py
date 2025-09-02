import numpy as np
from typing import List


class Retriever:
    """
    Mock Retriever to simulate Retrieval-Augmented Generation (RAG).
    Uses random embeddings and cosine similarity to find top-k similar bids.
    """

    def __init__(self) -> None:
        # Mock database of bids
        self.mock_bids = [
            "Healthcare service for elderly care",
            "Emergency room staffing request",
            "Telemedicine consultation package",
        ]

        # Random vectors to simulate embeddings
        np.random.seed(42)
        self.embeddings = np.random.rand(len(self.mock_bids), 5)

    def _embed(self, text: str) -> np.ndarray:
        """
        Generate a mock embedding vector for input text.

        Args:
            text (str): Input bid text.

        Returns:
            np.ndarray: 5-dimensional vector representation.
        """
        np.random.seed(abs(hash(text)) % (10**6))
        return np.random.rand(5)

    def find_similar_bids(self, bid_request: str, top_k: int = 2) -> List[str]:
        """
        Find top_k most similar stored bids to the given bid_request.

        Args:
            bid_request (str): The incoming healthcare bid text.
            top_k (int): Number of similar bids to return.

        Returns:
            List[str]: A list of similar bids.
        """
        query_vec = self._embed(bid_request)

        # Cosine similarity
        similarities = self.embeddings @ query_vec / (
            np.linalg.norm(self.embeddings, axis=1) * np.linalg.norm(query_vec)
        )

        top_indices = np.argsort(similarities)[::-1][:top_k]
        return [self.mock_bids[i] for i in top_indices]
