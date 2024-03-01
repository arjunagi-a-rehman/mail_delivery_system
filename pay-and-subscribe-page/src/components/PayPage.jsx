import React, { useState } from "react";
import axios from "axios";

const PayPage = ({ userId, price }) => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

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
    <div>
      <h1>Pay Page</h1>
      <p>Price: ${price}</p>
      <button onClick={handlePay} disabled={loading}>
        {loading ? "Paying..." : "Pay Now"}
      </button>
      {error && <p style={{ color: "red" }}>Error: {error}</p>}
    </div>
  );
};

export default PayPage;
