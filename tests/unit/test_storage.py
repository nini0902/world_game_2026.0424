import unittest

from src.services.storage import InMemoryStorage
from src.models.player_run import PlayerRun


class TestInMemoryStorage(unittest.TestCase):
    def test_create_get_update_run(self):
        storage = InMemoryStorage()
        run = PlayerRun()
        storage.create_run(run)

        fetched = storage.get_run(run.id)
        self.assertIsNotNone(fetched)
        self.assertEqual(fetched.id, run.id)

        # update
        fetched.current_node = "challenge"
        storage.update_run(fetched)
        updated = storage.get_run(run.id)
        self.assertEqual(updated.current_node, "challenge")


if __name__ == "__main__":
    unittest.main()
