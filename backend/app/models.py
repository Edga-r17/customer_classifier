from pydantic import BaseModel

class ClientData(BaseModel):
    salary: float
    expenses: float
