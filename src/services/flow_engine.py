import time
import logging
from src.models.player_run import PlayerRun, RunOutcome
from src.services.storage import InMemoryStorage

logger = logging.getLogger(__name__)


def start_run(storage: InMemoryStorage = None) -> PlayerRun:
    """Start a PlayerRun and advance through story->challenge->outcome.

    Logs structured events with run_id and current_node for observability.
    """
    if storage is None:
        storage = InMemoryStorage()

    run = PlayerRun()
    run.status = "in_progress"
    storage.create_run(run)
    logger.info("run_created", extra={"run_id": run.id, "status": run.status})

    run.current_node = "story"
    storage.update_run(run)
    logger.info("node_enter", extra={"run_id": run.id, "current_node": run.current_node})

    run.current_node = "challenge"
    storage.update_run(run)
    logger.info("node_enter", extra={"run_id": run.id, "current_node": run.current_node})

    run.current_node = "outcome"
    run.outcome = RunOutcome(result_type="success", message="Completed first run")
    run.status = "completed"
    storage.update_run(run)
    logger.info("run_completed", extra={"run_id": run.id, "status": run.status, "result": run.outcome.result_type})

    return run
