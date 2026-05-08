import express from "express";
import axios from "axios";

const app = express();
app.use(express.json());

const GEMINI_API_KEY = "TU_API_KEY";

const URL =
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=" +
  GEMINI_API_KEY;

app.post("/chat", async (req, res) => {
  try {
    const text = req.body.text;

    const response = await axios.post(URL, {
      contents: [{ parts: [{ text }] }],
    });

    const reply =
      response.data.candidates[0].content.parts[0].text;

    res.json({ reply });
  } catch (err: any) {
    res.json({ error: err.message });
  }
});

app.listen(3000, () => {
  console.log("Server running on port 3000");
});
