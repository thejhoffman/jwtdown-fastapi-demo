from fastapi import FastAPI
from authenticator import authenticator
from routers import accounts, protected

app = FastAPI()
app.include_router(authenticator.router)
app.include_router(accounts.router)
app.include_router(protected.router)
