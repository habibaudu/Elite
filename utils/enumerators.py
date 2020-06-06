from enum import Enum

class StateType(Enum):
    active = "active"
    deleted = "deleted"


class RequestStatus(Enum):
    pending = "pending"
    confirmed = "confirmed"
    rejected = "rejected"