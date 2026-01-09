from enum import Enum
from pydantic import BaseModel, PositiveFloat


class TrasnsactionType(Enum):
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"


class TransactionIn(BaseModel):
    account_id: int
    type: TrasnsactionType
    amount: PositiveFloat

    class Config:
        use_enum_values = True    