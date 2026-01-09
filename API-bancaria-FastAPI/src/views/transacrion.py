from pydantic import BaseModel, PositiveFloat, AwareDateTime, NaiveDateTime



class transactionOut(BaseModel):
    id: int
    account_id: int
    type: str
    amount: PositiveFloat
    timestamp: AwareDateTime | NaiveDateTime