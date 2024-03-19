from pydantic import BaseModel

class Config(BaseModel):
  length: float | None = None
  width: float | None = None
  cell: str | None = None
  color: str | None = None