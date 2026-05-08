from typing import Dict
from src.models.player_run import PlayerRun


class InMemoryStorage:
    def __init__(self):
        self._runs: Dict[str, PlayerRun] = {}

    def create_run(self, run: PlayerRun) -> PlayerRun:
        self._runs[run.id] = run
        return run

    def get_run(self, run_id: str):
        return self._runs.get(run_id)

    def update_run(self, run: PlayerRun) -> PlayerRun:
        self._runs[run.id] = run
        return run
