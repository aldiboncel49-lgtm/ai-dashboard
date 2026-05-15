import unittest
import json
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.report_generator import ReportGenerator


class TestReportGenerator(unittest.TestCase):

    def setUp(self):
        self.gen = ReportGenerator()

    def test_empty_history(self):
        # Tanpa file history, harus return no_data
        self.gen.history_path = "data/nonexistent.json"
        result = self.gen.generate_summary()
        self.assertEqual(result["status"], "no_data")

    def test_get_stats_empty(self):
        self.gen.history_path = "data/nonexistent.json"
        stats = self.gen.get_stats()
        self.assertEqual(stats["total"], 0)


if __name__ == "__main__":
    unittest.main()
