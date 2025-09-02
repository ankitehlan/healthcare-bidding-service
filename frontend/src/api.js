import axios from "axios";

const API_URL = "http://localhost:8000/bid-response/";

export const getBidResponse = async (bidRequest, context) => {
  const response = await axios.post(API_URL, {
    bid_request: bidRequest,
    context: context,
  });
  return response.data;
};
