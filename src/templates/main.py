from typing import List, Optional

from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field
from starlette.requests import Request

from src.classes.compound import Compound



app = FastAPI()

templates = Jinja2Templates(directory="templates")

# class Compound:

#     def __init__(self, name: str, x_cord: int, y_cord: int, ret_fact: float):

#         self.name = name    
#         self.x_cord = x_cord
#         self.y_cord = y_cord
#         self.ret_fact = ret_fact

class CompoundBase(BaseModel):
    compound_name: str = Field(..., min_length=1, max_length=15, description="Name of the compound")
    compound_ret_fact: float = Field(..., gt=0, min_length=2, description="Retention Factor of the compound")

@app.post("/simulate")
async def simulate(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


