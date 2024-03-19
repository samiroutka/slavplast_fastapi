import database
from sqlalchemy import Column, String, Integer, Float, ForeignKey

class Length(database.Base):
  __tablename__ = 'Lengths'
  id = Column(Integer, primary_key=True)
  length = Column(Float)

class Width(database.Base):
  __tablename__ = 'Widths'
  id = Column(Integer, primary_key=True)
  width = Column(Float)

class Cell(database.Base):
  __tablename__ = 'Cells'
  id = Column(Integer, primary_key=True)
  cell = Column(String)

class Color(database.Base):
  __tablename__ = 'Colors'
  id = Column(Integer, primary_key=True)
  color = Column(String)