from pydantic import BaseModel

class UserCreationData(BaseModel):
    name: str