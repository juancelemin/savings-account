

from fastapi import FastAPI
from routers import account, user



app = FastAPI()


app.include_router(account.router)
app.include_router(user.router)


