from fastapi import FastAPI,HTTPException
from pydantic import BaseModel, Field, field_validator

app = FastAPI()

BALANCE ={}

class OperationRequest(BaseModel):
    wallet_name: str = Field(..., max_length=100)
    amount: float
    description: str | None = Field(None, max_length=200)

    @field_validator('amount')
    def amount_is_positive(cls, v: float)-> float:
        if v <= 0:
            raise ValueError("Amount must be positive")
        return v

    @field_validator('wallet_name')
    def wallet_name_not_empty(cls, v: str)-> str:
        v = v.strip()
        if not v:
            raise ValueError("Wallet name cannot be empty")
        return v

class CreateWalletRequest(BaseModel):
    name: str = Field(..., max_length=100)
    initial_balance: float = 0

    @field_validator("name")
    def name_not_empty(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("Wallet name cannot be empty")
        return v

    @field_validator('initial_balance')
    def balance_not_negative(cls, v: float) -> float:
        if v < 0:
            raise ValueError("Initial balance must be positive")
        return v


@app.get("/balance")
def get_balance(wallet_name: str | None = None):
    if wallet_name is None:
        return {"total_balance": sum(BALANCE.values())}
    if wallet_name not in BALANCE:
        raise HTTPException(
            status_code=404,
            detail="Wallet not found"
        )
    return {"wallet": wallet_name, "balance": BALANCE[wallet_name]}

@app.post("/wallets")
def create_wallet(wallet: CreateWalletRequest):
    if wallet.name in BALANCE:
        raise HTTPException(
            status_code=400,
            detail=f"Wallet {wallet.name} already exists"
        )
    BALANCE[wallet.name] = wallet.initial_balance
    return {"wallet": wallet.name, "balance": wallet.initial_balance}

@app.post("/operations/income")
def add_income(operation: OperationRequest):
    if operation.wallet_name not in BALANCE:
        raise HTTPException(
            status_code=404,
            detail="Wallet not found"
        )
    BALANCE[operation.wallet_name] += operation.amount
    return{
        "message": "Income added",
        "wallet": operation.wallet_name,
        "amount": operation.amount,
        "description": operation.description,
        "new_balance": BALANCE[operation.wallet_name]
    }

@app.post("/operations/expense")
def add_expense(operation: OperationRequest):
    if operation.wallet_name not in BALANCE:
        raise HTTPException(
            status_code=404,
            detail="Wallet not found"
        )
    if operation.amount > BALANCE[operation.wallet_name]:
        raise HTTPException(
            status_code=400,
            detail="Amount exceeds balance"
        )
    BALANCE[operation.wallet_name] -= operation.amount
    return{
        "message": "Expense added",
        "wallet": operation.wallet_name,
        "amount": operation.amount,
        "description": operation.description,
        "new_balance": BALANCE[operation.wallet_name]
    }

#end at 30:00