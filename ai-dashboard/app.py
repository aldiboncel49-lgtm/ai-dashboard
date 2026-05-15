from flask import Flask, render_template, jsonify, request
from src.ai_analyzer import AIAnalyzer
from src.report_generator import ReportGenerator
import json

app = Flask(__name__)
analyzer = AIAnalyzer()
report_gen = ReportGenerator()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No text provided"}), 400
    result = analyzer.analyze(text)
    return jsonify(result)

@app.route("/api/report", methods=["GET"])
def get_report():
    report = report_gen.generate_summary()
    return jsonify(report)

@app.route("/api/stats", methods=["GET"])
def get_stats():
    stats = report_gen.get_stats()
    return jsonify(stats)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
