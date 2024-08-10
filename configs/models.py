import database
from sqlalchemy import Column, String, Integer, Float, ForeignKey

class Length(database.Base):
  __abstract__ = True
  id = Column(Integer, primary_key=True)
  length = Column(Float)

  def to_dict(self):
    return {column.name: getattr(self, column.name) for column in self.__table__.columns}

class Width(database.Base):
  __abstract__ = True
  id = Column(Integer, primary_key=True)
  width = Column(Float)

  def to_dict(self):
    return {column.name: getattr(self, column.name) for column in self.__table__.columns}

class Cell(database.Base):
  __abstract__ = True
  id = Column(Integer, primary_key=True)
  cell = Column(String)
  description = Column(String)
  
  def to_dict(self):
    return {column.name: getattr(self, column.name) for column in self.__table__.columns}

class Thickness(database.Base):
  __abstract__ = True
  id = Column(Integer, primary_key=True)
  thickness = Column(String)

  def to_dict(self):
    return {column.name: getattr(self, column.name) for column in self.__table__.columns}

class Color(database.Base):
  __abstract__ = True
  id = Column(Integer, primary_key=True)
  color = Column(String)

  def to_dict(self):
    return {column.name: getattr(self, column.name) for column in self.__table__.columns}

# --------------------------
type1 = 'Plastic'
class LengthPlastic(Length):
  __tablename__ = f'Lengths{type1}'

class WidthPlastic(Width):
  __tablename__ = f'Widths{type1}'

class CellPlastic(Cell):
  __tablename__ = f'Cells{type1}'

class ColorPlastic(Color):
  __tablename__ = f'Colors{type1}'

# --------------------------
type2 = 'Knotless'
class LengthKnotless(Length):
  __tablename__ = f'Lengths{type2}'

class WidthKnotless(Width):
  __tablename__ = f'Widths{type2}'

class CellKnotless(Cell):
  __tablename__ = f'Cells{type2}'

class ThicknessKnotless(Thickness):
  __tablename__ = f'Thickness{type2}'
