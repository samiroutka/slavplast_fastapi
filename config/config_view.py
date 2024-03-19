
from fastapi import APIRouter, Depends
import database
from . import models, schemas

router = APIRouter(tags=['config'], prefix='/config')

config_models = {
  'length': models.Length,
  'width': models.Width,
  'cell': models.Cell,
  'color': models.Color,
}

@router.get('')
def get_config(db = Depends(database.get_session)):
  config = {}
  for item in config_models:
    item_elements = db.query(config_models[item]).all()
    if item_elements:
      config[item] = item_elements
  return config

@router.post('')
def add_config(body: schemas.Config, db = Depends(database.get_session)):
  print(dict(body))
  for config_item in dict(body):
    if dict(body)[config_item] != None:
      new_config_item = config_models[config_item](**{config_item: dict(body)[config_item]})
      db.add(new_config_item)
      db.commit()
      db.refresh(new_config_item)
  return new_config_item

@router.delete('/{type}/{id}')
def delete_config(type: str, id: int, db = Depends(database.get_session)):
  db.query(config_models[type]).filter(config_models[type].id == id).delete()
  db.commit()
  return True

