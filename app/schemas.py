from pydantic import BaseModel , ValidationError
from typing import *

class PostCreate(BaseModel):
    name:str
    age:int
    email:str    

class PostResponse(BaseModel):
    name:str
    age:int
    email:str    

class PostPatch(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[str] = None

