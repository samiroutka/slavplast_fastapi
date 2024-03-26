import database
from sqlalchemy import Column, String, Integer, ARRAY, ForeignKey, text
from sqlalchemy.orm import relationship

class NetPlastic(database.Base):
  type = 'Plastic'
  __tablename__ = f'Nets{type}'
  id = Column(Integer, primary_key=True)
  images = Column(ARRAY(String))
  length = Column(Integer, ForeignKey(f'Lengths{type}.id', ondelete='CASCADE'))
  width = Column(Integer, ForeignKey(f'Widths{type}.id', ondelete='CASCADE'))
  cell = Column(Integer, ForeignKey(f'Cells{type}.id', ondelete='CASCADE'))
  color = Column(Integer, ForeignKey(f'Colors{type}.id', ondelete='CASCADE'))

class NetKnotless(database.Base):
  type = 'Knotless'
  __tablename__ = f'Nets{type}'
  id = Column(Integer, primary_key=True)
  images = Column(ARRAY(String))
  length = Column(Integer, ForeignKey(f'Lengths{type}.id', ondelete='CASCADE'))
  width = Column(Integer, ForeignKey(f'Widths{type}.id', ondelete='CASCADE'))
  cell = Column(Integer, ForeignKey(f'Cells{type}.id', ondelete='CASCADE'))
  thickness = Column(Integer, ForeignKey(f'Thickness{type}.id', ondelete='CASCADE'))
