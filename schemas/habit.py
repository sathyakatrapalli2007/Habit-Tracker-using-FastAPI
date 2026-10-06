from pydantic import BaseModel,Field
from datetime import date
from enum import Enum

class status(str,Enum):
    DONE="done"
    NOT_DONE="not done"

class Habit(BaseModel):
    id:str
    name:str
    description:str
    logs:dict[date,status]=Field(default_factory=lambda:{})

class HabitCreate(BaseModel):
    name:str
    description:str

class HabitRead(BaseModel):
    id:str
    name:str
    description:str
    logs:dict[date,status]=Field(default_factory=lambda:{})

class HabitUpdate(BaseModel):  
    name:str|None
    description:str|None
    
class LogUpdate(BaseModel):
    status:status|None          
    date:date|None