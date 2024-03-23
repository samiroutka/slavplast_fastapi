
from fastapi import APIRouter, Depends
from typing import Union
import database
from . import models, schemas

router = APIRouter(tags=['nets'])

net_models = {
  'plastic': models.NetPlastic,
  'knotless': models.NetKnotless
}

@router.get('/nets/{netType}')
def get_nets(netType: str, db = Depends(database.get_session)):
  return db.query(net_models[netType]).all()

@router.get('/net/{netType}/{id}')
def get_nets(id: int,netType: str, db = Depends(database.get_session)):
  return db.query(net_models[netType]).filter(net_models[netType].id == id).first()

@router.post('/net/{netType}', response_model=bool)
def add_net(body: Union[schemas.NetPlastic, schemas.NetKnotless], netType: str, db = Depends(database.get_session)):
  new_net = net_models[netType](**dict(body))
  print('new_net', new_net)
  db.add(new_net)
  db.commit()
  return True

@router.put('/net/{netType}/{id}', response_model=bool)
def get_nets(id: int, body: Union[schemas.NetPlastic, schemas.NetKnotless], netType: str, db = Depends(database.get_session)):
  db.query(net_models[netType]).filter(net_models[netType].id == id).update(dict(body))
  db.commit()
  return True

@router.delete('/net/{netType}/{id}', response_model=bool)
def get_nets(id: int,netType: str, db = Depends(database.get_session)):
  db.query(net_models[netType]).filter(net_models[netType].id == id).delete()
  db.commit()
  return True