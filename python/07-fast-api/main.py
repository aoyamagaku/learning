from fastapi import FastAPI,HTTPException
from app.api.v1.wallets import router as wallet_router
from app.api.v1.wallets import router as operations_router

app = FastAPI()

app.include_router(wallet_router, prefix="/api/v1", tags=["wallet"])
app.include_router(operations_router, prefix="/api/v1", tags=["operations"])

#end at 43:58