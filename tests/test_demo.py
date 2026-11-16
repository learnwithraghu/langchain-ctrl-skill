import os
import subprocess
import sys
import unittest
from unittest.mock import patch

import demo
from langchain_core.messages import AIMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda


class DemoTests(unittest.TestCase):
    def test_refund_retrieval_and_unknown_query(self):
        self.assertIn("[refunds]", demo.retrieve("How do I get a refund?"))
        self.assertEqual(demo.retrieve("quantum bananas"), "No matching snippets found.")

    def test_prepared_prompt_and_chain(self):
        messages = demo.prepare.invoke("When are Python workshops?").to_messages()
        self.assertIn("[schedule]", messages[1].content)
        chain = demo.prepare | RunnableLambda(lambda _: AIMessage(content="Test [schedule]")) | StrOutputParser()
        self.assertEqual(chain.invoke("When are Python workshops?"), "Test [schedule]")

    def test_dry_run_and_missing_key(self):
        env = os.environ.copy()
        env.pop("OPENROUTER_API_KEY", None)
        dry = subprocess.run([sys.executable, "demo.py", "--dry-run"], env=env,
                             capture_output=True, text=True)
        self.assertEqual(dry.returncode, 0)
        self.assertIn("[refunds]", dry.stdout)
        live = subprocess.run([sys.executable, "demo.py"], env=env,
                              capture_output=True, text=True)
        self.assertNotEqual(live.returncode, 0)
        self.assertIn("Set OPENROUTER_API_KEY", live.stderr)

    def test_live_chain_with_fake_model(self):
        with patch.dict(os.environ, {"OPENROUTER_API_KEY": "test-key"}), \
             patch.object(demo, "ChatOpenRouter",
                          return_value=RunnableLambda(lambda _: AIMessage(content="14 days [refunds]"))), \
             patch.object(sys, "argv", ["demo.py"]):
            self.assertEqual(demo.main(), 0)


if __name__ == "__main__":
    unittest.main()
