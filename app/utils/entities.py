from dataclasses import dataclass
from datetime import datetime
from typing import Tuple, Any

JSONResponse = Tuple[Any, int]


@dataclass
class SerializedUser:
    user_id: int
    username: str
    email: str
    full_name: str
    created_at: datetime


@dataclass
class UserSession:
    user_id: int
    username: str
