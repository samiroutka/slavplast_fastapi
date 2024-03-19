import database
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

class Net(database.Base):
  __tablename__ = 'Nets'

  id = Column(Integer, primary_key=True)
  length = Column(Integer, ForeignKey('Lengths.id', ondelete='CASCADE'))
  width = Column(Integer, ForeignKey('Widths.id', ondelete='CASCADE'))
  cell = Column(Integer, ForeignKey('Cells.id', ondelete='CASCADE'))
  color = Column(Integer, ForeignKey('Colors.id', ondelete='CASCADE'))