import { useState } from "react";

export default function MatchForm() {
  const [formData, setFormData] = useState({
    name: "",
    strength: "",
    weakness: "",
    location: ""
  });

  const [match, setMatch] = useState(null);
  const [status, setStatus] = useState("");

  const handleChange = (e) => {
    setFormData(prev => ({ ...prev, [e.target.name]: e.target.value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setStatus("Submitting...");

    try {
      const res = await fetch("http://localhost:8001/submit", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData)
      });

      const data = await res.json();
      setMatch(data.match);
      setStatus(data.status === "match_found" ? "Match found!" : "No match yet.");
    } catch (err) {
      console.error("Error:", err);
      setStatus("Error connecting to backend.");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>Find a Match</h2>
      <form onSubmit={handleSubmit}>
        <input name="name" placeholder="Name" onChange={handleChange} /><br />
        <input name="strength" placeholder="Strengths (comma separated)" onChange={handleChange} /><br />
        <input name="weakness" placeholder="Weaknesses (comma separated)" onChange={handleChange} /><br />
        <input name="location" placeholder="Location" onChange={handleChange} /><br />
        <button type="submit">Submit</button>
      </form>

      <p>{status}</p>

      {match && (
        <div style={{ marginTop: "20px" }}>
          <h3>Your Match:</h3>
          <p><strong>Name:</strong> {match.Name}</p>
          <p><strong>Strengths:</strong> {match.Strengths}</p>
          <p><strong>Location:</strong> {match.Location}</p>
        </div>
      )}
    </div>
  );
}
