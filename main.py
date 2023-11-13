from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
from router import router

app = FastAPI()

app.include_router(router)