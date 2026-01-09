from pydantic import AwareDateTime, BaseModel, NaiveDateTime , PositiveFloat


class AccountOut(BaseModel):
    id: int
    user_id: int
    balance: float
    created_at: AwareDateTime | NaiveDateTime


class TransactionOut(BaseModel):
    id: int
    account_id: int
    type: str
    amount: PositiveFloat
    timestamp: AwareDateTime | NaiveDateTime
