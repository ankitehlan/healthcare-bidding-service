import React, { useState } from "react";
import { getBidResponse } from "../api";

function BidForm() {
  const [bidRequest, setBidRequest] = useState("");
  const [context, setContext] = useState("");
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const data = await getBidResponse(bidRequest, context);
      setResponse(data);
    } catch (error) {
      console.error(error);
      alert("Error fetching response.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <form
        onSubmit={handleSubmit}
        style={{ display: "flex", flexDirection: "column", gap: "10px" }}
      >
        <textarea
          placeholder="Enter healthcare bid request"
          value={bidRequest}
          onChange={(e) => setBidRequest(e.target.value)}
          required
          style={{ padding: "10px", minHeight: "80px" }}
        />
        <input
          type="text"
          placeholder="Optional context"
          value={context}
          onChange={(e) => setContext(e.target.value)}
          style={{ padding: "10px" }}
        />
        <button type="submit" disabled={loading}>
          {loading ? "Submitting..." : "Submit"}
        </button>
      </form>

      {response && (
        <div
          style={{ marginTop: "20px", padding: "10px", border: "1px solid #ccc" }}
        >
          <h3>Results</h3>
          <p>
            <strong>Gemini Answer:</strong> {response.gemini_answer}
          </p>
          <p>
            <strong>Custom LLM Answer:</strong>{" "}
            {response.custom_llm_expected_answer}
          </p>
        </div>
      )}
    </div>
  );
}

export default BidForm;
