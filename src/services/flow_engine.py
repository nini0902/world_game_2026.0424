import time
from src.models.player_run import PlayerRun, RunOutcome
from src.services.storage import InMemoryStorage


def start_run(storage: InMemoryStorage = None) -> PlayerRun:
    if storage is None:
        storage = InMemoryStorage()

    run = PlayerRun()
    run.status = "in_progress"
    storage.create_run(run)

    run.current_node = "story"
    storage.update_run(run)

    run.current_node = "challenge"
    storage.update_run(run)

    run.current_node = "outcome"
    run.outcome = RunOutcome(result_type="success", message="Completed first run")
    run.status = "completed"
    storage.update_run(run)

    return run
