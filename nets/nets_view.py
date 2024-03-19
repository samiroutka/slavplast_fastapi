
from fastapi import APIRouter, Depends
import database
from . import models, schemas

router = APIRouter(tags=['nets'])

@router.get('/nets')
def get_nets(db = Depends(database.get_session)):
  return db.query(models.Net).all()

@router.get('/net/{id}')
def get_nets(id: int, db = Depends(database.get_session)):
  return db.query(models.Net).filter(models.Net.id == id).first()

@router.post('/net', response_model=bool)
def add_net(body: schemas.Net, db = Depends(database.get_session)):
  new_net = models.Net(**dict(body))
  db.add(new_net)
  db.commit()
  return True

@router.put('/net/{id}', response_model=bool)
def get_nets(id: int, body: schemas.Net, db = Depends(database.get_session)):
  db.query(models.Net).filter(models.Net.id == id).update(dict(body))
  db.commit()
  return True

@router.delete('/net/{id}', response_model=bool)
def get_nets(id: int, db = Depends(database.get_session)):
  db.query(models.Net).filter(models.Net.id == id).delete()
  db.commit()
  return True