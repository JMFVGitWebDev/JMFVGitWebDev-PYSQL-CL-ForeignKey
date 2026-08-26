from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class User:
    id: int = 0
    firstname: Optional[str] = None
    lastname: Optional[str] = None
