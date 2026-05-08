import unittest


class TestFullFlowE2E(unittest.TestCase):
    def test_full_flow_runs_to_outcome(self):
        """End-to-end smoke test for the newbie core loop.

        This test is intentionally failing as the implementation is not yet present.
        TDD: create this failing test first, then implement minimal code to make it pass.
        """
        from src.services.flow_engine import start_run
        from src.services.storage import InMemoryStorage

        storage = InMemoryStorage()
        run = start_run(storage=storage)

        self.assertEqual(run.status, "completed")
        self.assertIsNotNone(run.outcome)
        self.assertEqual(run.outcome.result_type, "success")


if __name__ == "__main__":
    unittest.main()
