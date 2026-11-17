import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]

class ReferenceFixtureTests(unittest.TestCase):
    def test_bt001_expected_value_and_return(self):
        data = json.loads((ROOT / "examples/hypothetical-input.json").read_text())
        output = json.loads((ROOT / "examples/hypothetical-output.json").read_text())
        initial = data["portfolio"]["initial_capital"]
        prices = data["market_data"]["series"]
        expected = sum(initial * p["target_weight"] *
            prices[-1]["prices"][p["asset_id"]] / prices[0]["prices"][p["asset_id"]]
            for p in data["portfolio"]["positions"])
        self.assertAlmostEqual(expected, 10800.0, places=8)
        self.assertAlmostEqual(output["portfolio_timeseries"][-1]["value"], expected, places=8)
        self.assertAlmostEqual(output["performance"]["total_return"], expected / initial - 1, places=10)
        self.assertEqual(output["status"], "partial")

    def test_visualization_fixture_matches_equity_series(self):
        output = json.loads((ROOT / "examples/hypothetical-output.json").read_text())
        viz = json.loads((ROOT / "examples/hypothetical-visualization-handoff.json").read_text())
        self.assertEqual(viz["series"][0]["points"], output["portfolio_timeseries"])
