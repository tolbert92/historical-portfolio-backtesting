import copy
import json
import pathlib
import unittest
from jsonschema import Draft202012Validator, FormatChecker, ValidationError

ROOT = pathlib.Path(__file__).resolve().parents[1]

def load(path):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))

class ContractTests(unittest.TestCase):
    def test_schemas_are_valid(self):
        for name in ("backtest-input", "backtest-output", "visualization-handoff"):
            with self.subTest(schema=name):
                Draft202012Validator.check_schema(load(f"schemas/{name}.schema.json"))

    def test_example_inputs_validate(self):
        cases = (("backtest-input", "hypothetical-input"),
                 ("backtest-output", "hypothetical-output"),
                 ("visualization-handoff", "hypothetical-visualization-handoff"))
        for schema, fixture in cases:
            with self.subTest(fixture=fixture):
                Draft202012Validator(load(f"schemas/{schema}.schema.json"),
                    format_checker=FormatChecker()).validate(load(f"examples/{fixture}.json"))

    def test_rejects_invalid_weights_type(self):
        fixture = load("examples/hypothetical-input.json")
        fixture["portfolio"]["positions"][0]["target_weight"] = "sixty percent"
        with self.assertRaises(ValidationError):
            Draft202012Validator(load("schemas/backtest-input.schema.json")).validate(fixture)

    def test_rejects_missing_required_input(self):
        fixture = load("examples/hypothetical-input.json")
        del fixture["market_data"]
        with self.assertRaises(ValidationError):
            Draft202012Validator(load("schemas/backtest-input.schema.json")).validate(fixture)

    def test_rejects_invalid_status(self):
        fixture = load("examples/hypothetical-output.json")
        fixture["status"] = "magically_complete"
        with self.assertRaises(ValidationError):
            Draft202012Validator(load("schemas/backtest-output.schema.json")).validate(fixture)
