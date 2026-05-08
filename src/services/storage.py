from typing import Dict
from src.models.player_run import PlayerRun


class InMemoryStorage:
    def __init__(self):
        self._runs: Dict[str, PlayerRun] = {}
        import logging
        self._logger = logging.getLogger(__name__)

    def create_run(self, run: PlayerRun) -> PlayerRun:
        self._runs[run.id] = run
        # basic observability
        try:
            self._logger.debug("create_run", extra={"run_id": run.id, "status": run.status})
        except Exception:
            pass
        return run

    def get_run(self, run_id: str):
        return self._runs.get(run_id)

    def update_run(self, run: PlayerRun) -> PlayerRun:
        self._runs[run.id] = run
        try:
            self._logger.debug("update_run", extra={"run_id": run.id, "current_node": run.current_node, "status": run.status})
        except Exception:
            pass
        return run
