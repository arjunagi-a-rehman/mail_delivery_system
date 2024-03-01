import React, { useState } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";

const PayPage = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  let { userId } = useParams();
  const handlePay = async () => {
    try {
      setLoading(true);
      await axios.post(`http://localhost:8000/api/user/${userId}/subscribe`);
      alert("Payment successful!");
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container-fluid text-center">
      <h1>Pay Page</h1>
      <p>Price: 20000 rs</p>
      <button onClick={handlePay} disabled={loading}>
        {loading ? "Paying..." : "Pay Now"}
      </button>
      {error && <p style={{ color: "red" }}>Error: {error}</p>}
    </div>
  );
};

export default PayPage;
