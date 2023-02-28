

from fastapi import FastAPI
from routers import accounts



app = FastAPI(
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)
app.include_router(accounts.router)
