import json
import os
from datetime import datetime
from collections import Counter


class ReportGenerator:
    def __init__(self):
        self.history_path = "data/analysis_history.json"

    def _load_history(self) -> list:
        if not os.path.exists(self.history_path):
            return []
        with open(self.history_path, "r") as f:
            return json.load(f)

    def generate_summary(self) -> dict:
        """Generate a summary report from all past analyses."""
        history = self._load_history()
        if not history:
            return {"status": "no_data", "message": "No analyses found."}

        sentiments = [h["result"].get("sentiment", "neutral") for h in history]
        risks = [h["result"].get("risk_level", "low") for h in history]
        all_topics = []
        for h in history:
            all_topics.extend(h["result"].get("key_topics", []))

        top_topics = [t for t, _ in Counter(all_topics).most_common(5)]
        sentiment_dist = dict(Counter(sentiments))
        risk_dist = dict(Counter(risks))

        return {
            "status": "success",
            "total_analyses": len(history),
            "sentiment_distribution": sentiment_dist,
            "risk_distribution": risk_dist,
            "top_topics": top_topics,
            "latest_analysis": history[-1]["timestamp"] if history else None,
            "generated_at": datetime.now().isoformat()
        }

    def get_stats(self) -> dict:
        """Get quick stats for the dashboard."""
        history = self._load_history()
        if not history:
            return {
                "total": 0,
                "positive": 0,
                "negative": 0,
                "neutral": 0,
                "high_risk": 0
            }

        sentiments = [h["result"].get("sentiment", "neutral") for h in history]
        risks = [h["result"].get("risk_level", "low") for h in history]

        return {
            "total": len(history),
            "positive": sentiments.count("positive"),
            "negative": sentiments.count("negative"),
            "neutral": sentiments.count("neutral"),
            "high_risk": risks.count("high"),
            "chart_data": self._build_chart_data(history)
        }

    def _build_chart_data(self, history: list) -> list:
        """Build last 7 entries for chart display."""
        recent = history[-7:]
        return [
            {
                "date": h["timestamp"][:10],
                "sentiment_score": h["result"].get("sentiment_score", 0.5),
                "risk": h["result"].get("risk_level", "low")
            }
            for h in recent
        ]
