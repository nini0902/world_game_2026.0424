import unittest

from src.services.flow_engine import start_run
from src.services.storage import InMemoryStorage


class TestFlowEngine(unittest.TestCase):
    def test_start_run_completes(self):
        storage = InMemoryStorage()
        run = start_run(storage=storage)

        self.assertEqual(run.status, "completed")
        self.assertEqual(run.current_node, "outcome")
        self.assertIsNotNone(run.outcome)


if __name__ == "__main__":
    unittest.main()
