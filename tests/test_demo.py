import importlib.util
import os
import unittest
from pathlib import Path
from unittest.mock import patch


def load_demo(number):
    path = Path(__file__).resolve().parents[1] / "demos" / f"demo-{number:02}.py"
    spec = importlib.util.spec_from_file_location(f"demo_{number:02}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


retrieval_demo = load_demo(4)
provider_demo = load_demo(5)


class DemoTests(unittest.TestCase):
    def test_retrieval_matches_topic_and_handles_unknown(self):
        self.assertIn("14 days", retrieval_demo.retrieve("How do I get a refund?"))
        self.assertEqual(
            retrieval_demo.retrieve("What is the parking fee?"),
            "No matching information.",
        )

    def test_provider_selection_reuses_chat_model_interface(self):
        with patch.dict(os.environ, {
            "OPENAI_MODEL": "gpt-4o-mini",
            "OPENROUTER_MODEL": "openrouter/free",
        }), patch.object(provider_demo, "ChatOpenAI") as openai:
            provider_demo.get_model("openai")
            openai.assert_called_once_with(model="gpt-4o-mini")

        with patch.dict(os.environ, {
            "OPENAI_MODEL": "gpt-4o-mini",
            "OPENROUTER_MODEL": "openrouter/free",
        }), patch.object(provider_demo, "ChatOpenRouter") as openrouter:
            provider_demo.get_model("openrouter")
            openrouter.assert_called_once_with(model="openrouter/free")

        with self.assertRaises(ValueError):
            provider_demo.get_model("unsupported")


if __name__ == "__main__":
    unittest.main()
