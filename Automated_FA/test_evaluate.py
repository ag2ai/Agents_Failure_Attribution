import json
import tempfile
import unittest
from pathlib import Path

from Automated_FA.evaluate import evaluate_accuracy


class EvaluateAccuracyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.data_path = Path(self.temp_dir.name)
        (self.data_path / "synthetic.json").write_text(
            json.dumps({"mistake_agent": "agent_1", "mistake_step": 1}),
            encoding="utf-8",
        )

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_prefixes_are_not_exact_agent_or_step_matches(self) -> None:
        predictions = {
            "synthetic.json": {
                "predicted_agent": "agent_10",
                "predicted_step": "10",
            }
        }

        accuracy = evaluate_accuracy(predictions, str(self.data_path), total_files=1)

        self.assertEqual(accuracy, (0.0, 0.0))

    def test_exact_agent_and_step_matches_are_correct(self) -> None:
        predictions = {
            "synthetic.json": {
                "predicted_agent": "agent_1",
                "predicted_step": "1",
            }
        }

        accuracy = evaluate_accuracy(predictions, str(self.data_path), total_files=1)

        self.assertEqual(accuracy, (100.0, 100.0))


if __name__ == "__main__":
    unittest.main()
