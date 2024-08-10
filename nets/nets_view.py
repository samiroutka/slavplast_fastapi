
from fastapi import APIRouter, Depends, UploadFile, HTTPException
from fastapi.responses import FileResponse
from typing import Union, Dict
import database
from . import models, schemas
import configs.models
from configs.configs_view import get_config

router = APIRouter(tags=['nets'])

net_models = {
  'plastic': models.NetPlastic,
  'knotless': models.NetKnotless
}

def changeNetsWithConfig(netType, db, nets): # преобразуем id в свойствах сетки в их реальные свойства по конфигам
  config = get_config(netType, db)
  nets = list(map(lambda net: net.to_dict(), nets))
  new_nets = []
  for net in nets:
    for key, value in net.items():
      try: net[key] = getattr(list(filter(lambda item: item.id == value, config[key]))[0], key) # фильтруем config и получаем нужное свойство по id
      except: pass
    new_nets.append(net)
  return new_nets

@router.get('/nets/{netType}')
def get_nets(netType: str, db = Depends(database.get_session)):
  return changeNetsWithConfig(netType, db, db.query(net_models[netType]).all())

@router.get('/net/{netType}/{id}')
def get_nets(id: int, netType: str, db = Depends(database.get_session)):
  return changeNetsWithConfig(netType, db, db.query(net_models[netType]).filter(net_models[netType].id == id).all())[0]

@router.post('/net/{netType}', response_model=bool)
def add_net(body: Union[schemas.NetPlastic, schemas.NetKnotless], netType: str, db = Depends(database.get_session)):
  print('dict(body)', dict(body))
  print('net_models[netType]', net_models[netType])
  new_net = net_models[netType](**dict(body))
  db.add(new_net)
  db.commit()
  return True

@router.put('/net/{netType}/{id}', response_model=bool)
def update_nets(id: int, body: dict, netType: str, db = Depends(database.get_session)):
  print(dict(body))
  db.query(net_models[netType]).filter(net_models[netType].id == id).update(dict(body))
  db.commit()
  return True

@router.delete('/net/{netType}/{id}', response_model=bool)
def get_nets(id: int,netType: str, db = Depends(database.get_session)):
  db.query(net_models[netType]).filter(net_models[netType].id == id).delete()
  db.commit()
  return True

# -------------------------------

cells_models = {
  'plastic': configs.models.CellPlastic,
  'knotless': configs.models.CellKnotless,
}

@router.get('/cells/{netType}')
def get_cells(netType: str, db = Depends(database.get_session)):
  cells = db.query(cells_models[netType]).all()
  cells = list(filter(lambda cell: db.query(net_models[netType]).filter(net_models[netType].cell == cell.id).first(), cells))
  return cells

@router.get('/cells/{netType}/{cellId}')
def get_nets_byCells(netType: str, cellId: int, db = Depends(database.get_session)):
  return changeNetsWithConfig(netType, db, db.query(net_models[netType]).filter(net_models[netType].cell == cellId).all())
  
@router.put('/cells/{netType}/{cellId}')
def update_cell(body: dict, netType: str, cellId: int, db = Depends(database.get_session)):
  db.query(cells_models[netType]).filter(cells_models[netType].id == cellId).update(dict(body))
  db.commit()
  return True
