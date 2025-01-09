
from pydantic import BaseModel

# class which will describe BankNotes measurements
class BankNote(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float