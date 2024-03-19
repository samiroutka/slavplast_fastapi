from pydantic import BaseModel

class Net(BaseModel):
  # это все id конфигов
  length: int
  width: int
  cell: int
  color: int
