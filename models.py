from pydantic import BaseModel

class Pet(BaseModel):
    id: int
    category: dict
    name: str
    photoUrls: list
    tags: list
    status: str