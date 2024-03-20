
from fastapi import APIRouter, Depends
import database
from . import models, schemas
from nets.models import Net

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
  for config_item in dict(body):
    if dict(body)[config_item] != None:
      new_config_item = config_models[config_item](**{config_item: dict(body)[config_item]})
      db.add(new_config_item)
      db.commit()
      db.refresh(new_config_item)
  return new_config_item

@router.delete('/{type}/{id}')
def delete_config(type: str, id: int, force: bool | None = None, db = Depends(database.get_session)):
  def nets_relate_with_config():
    delete_element = db.query(config_models[type]).filter(config_models[type].id == id).first()
    existing_nets = db.query(Net).filter(getattr(Net, type) == delete_element.id).all()
    return existing_nets

  current_nets = nets_relate_with_config()

  if len(current_nets) == 0 and not force:
    db.query(config_models[type]).filter(config_models[type].id == id).delete()
    db.commit()
    return True
  elif force:
    db.query(config_models[type]).filter(config_models[type].id == id).delete()
    for net in current_nets:
      db.delete(net)
      db.commit()
  else:
    return False

