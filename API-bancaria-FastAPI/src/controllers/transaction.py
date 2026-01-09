from fastapi import APIRouter, Depends, status

from src.schemas.transaction import TrasactionIn
from src.security import login_required
from src.services.transaction import TransactionService
from src.views.transaction import TrasactionOut



router = APIRouter(prefix="/transactions", dependencies=[Depends(login_required)])

service = TransactionService()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=TrasactionOut)
async def create_transaction(trasaction: TrasactionIn):
    return await service.create(trasaction)

