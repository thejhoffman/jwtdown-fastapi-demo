from fastapi import APIRouter, Depends
from authenticator import authenticator

router = APIRouter(tags=["Protected"])


@router.get("/api/protected", response_model=bool)
async def get_protected(
    account_data: dict = Depends(authenticator.get_current_account_data),
):
    return True
