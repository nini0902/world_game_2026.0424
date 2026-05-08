from dataclasses import dataclass, field
from typing import Optional
import uuid
import time


@dataclass
class RunOutcome:
    result_type: str
    message: str


@dataclass
class PlayerRun:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    start_time: float = field(default_factory=time.time)
    current_node: str = "start"
    status: str = "initialized"
    outcome: Optional[RunOutcome] = None
