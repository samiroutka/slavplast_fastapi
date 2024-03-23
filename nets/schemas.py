from pydantic import BaseModel

class NetPlastic(BaseModel):
  # это все id конфигов
  length: int
  width: int
  cell: int
  color: int
  
class NetKnotless(BaseModel):
  # это все id конфигов
  length: int
  width: int
  cell: int
  thickness: int
