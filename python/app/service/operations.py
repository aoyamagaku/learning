from fastapi import HTTPException

from app.schemas import OperationRequest
from app.repository import wallets as wallets_repository


def add_income(operation: OperationRequest):
    if wallets_repository.if_wallet_exists():
        raise HTTPException(
            status_code=404,
            detail="Wallet not found"
        )
    new_balance = wallets_repository.add_income(operation.wallet_name, operation.amount)

    return{
        "message": "Income added",
        "wallet": operation.wallet_name,
        "amount": operation.amount,
        "description": operation.description,
        "new_balance": new_balance
    }

def add_expense(operation: OperationRequest):
    if wallets_repository.if_wallet_exists():
        raise HTTPException(
            status_code=404,
            detail="Wallet not found"
        )

    balance = wallets_repository.get_wallet_balance_by_name(operation.wallet_name)
    if balance < operation.amount:
        raise HTTPException(
            status_code=400,
            detail=f"Amount exceeds balance. Available: {balance}"
        )

    new_balance = wallets_repository.add_expense(operation.wallet_name, operation.amount)

    return{
        "message": "Expense added",
        "wallet": operation.wallet_name,
        "amount": operation.amount,
        "description": operation.description,
        "new_balance": new_balance
    }
