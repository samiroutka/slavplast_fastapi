from pydantic import BaseModel
from typing import Union

class NetPlastic(BaseModel):
  # это все id конфигов
  images: list 
  length: int 
  width: int 
  cell: int 
  color: int
  price: int
  quantity: int
  
class NetKnotless(BaseModel):
  # это все id конфигов
  images: list
  length: int
  width: int
  cell: int
  thickness: int
  price: int
  quantity: int
