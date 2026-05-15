import os
import anthropic
from datetime import datetime


class AIAnalyzer:
    def __init__(self):
        self.client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))
        self.history = []

    def analyze(self, text: str) -> dict:
        """Analyze text using Claude AI and return structured report."""
        prompt = f"""Analyze the following business text and provide a structured JSON report.
Return ONLY valid JSON with this structure:
{{
  "summary": "brief summary in 1-2 sentences",
  "sentiment": "positive | neutral | negative",
  "sentiment_score": 0.0 to 1.0,
  "key_topics": ["topic1", "topic2", "topic3"],
  "action_items": ["action1", "action2"],
  "risk_level": "low | medium | high",
  "insights": "1-2 sentence business insight"
}}

Text to analyze:
{text}"""

        try:
            message = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=1024,
                messages=[{"role": "user", "content": prompt}]
            )

            raw = message.content[0].text.strip()
            # Strip markdown code fences if present
            if raw.startswith("```"):
                raw = raw.split("```")[1]
                if raw.startswith("json"):
                    raw = raw[4:]
            import json
            result = json.loads(raw.strip())

            entry = {
                "timestamp": datetime.now().isoformat(),
                "input_length": len(text),
                "result": result
            }
            self.history.append(entry)
            self._save_history()

            return {"status": "success", "data": result, "timestamp": entry["timestamp"]}

        except Exception as e:
            return {"status": "error", "message": str(e)}

    def _save_history(self):
        import json
        os.makedirs("data", exist_ok=True)
        with open("data/analysis_history.json", "w") as f:
            json.dump(self.history, f, indent=2)

    def get_history(self) -> list:
        return self.history
