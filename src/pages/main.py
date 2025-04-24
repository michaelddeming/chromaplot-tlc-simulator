from typing import List, Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

api = FastAPI()

# class Compound:

#     def __init__(self, name: str, x_cord: int, y_cord: int, ret_fact: float):

#         self.name = name    
#         self.x_cord = x_cord
#         self.y_cord = y_cord
#         self.ret_fact = ret_fact

class CompoundBase(BaseModel):
    compound_name: str = Field(..., min_length=1, max_length=15, description="Name of the compound")
    compound_x_cord: int = Field(..., min_length=1, description="X-cord of the compound")
    compound_y_cord: int = Field(..., min_length=1, description="Y-cord of the compound")
    compound_ret_fact: float = Field(..., min_length=2, description="Retention Factor of the compound")


@api.get("/")
def home():
    return "<h1>Hello</h1>"