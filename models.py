from pydantic import BaseModel, HttpUrl, Field

class ServiceCreate(BaseModel):
    name: str = Field (min_length=1)
    url: HttpUrl