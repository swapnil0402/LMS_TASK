from fastapi import FastAPI
from collections.abc import MutableMapping
from collections import namedtuple
from route.routes import router

app = FastAPI()
app.include_router(router)