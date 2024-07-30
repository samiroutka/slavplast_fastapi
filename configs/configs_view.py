
from fastapi import APIRouter, Depends
import database
from . import models, schemas
from nets.models import NetPlastic, NetKnotless

router = APIRouter(tags=['config'], prefix='/config')

config_models_plastic = {
  'length': models.LengthPlastic,
  'width': models.WidthPlastic,
  'cell': models.CellPlastic,
  'color': models.ColorPlastic,
}
config_models_knotless = {
  'length': models.LengthKnotless,
  'width': models.WidthKnotless,
  'cell': models.CellKnotless,
  'thickness': models.ThicknessKnotless,
}

@router.get('/{netType}')
def get_config(netType: str, db = Depends(database.get_session)):
  config = {}
  config_models = config_models_plastic if netType == 'plastic' else config_models_knotless
  for item in config_models:
    item_elements = db.query(config_models[item]).order_by('id').all()
    if item_elements:
      config[item] = item_elements
  return config

@router.post('/{netType}')
def add_config(netType: str, body: schemas.Config, db = Depends(database.get_session)):
  config_models = config_models_plastic if netType == 'plastic' else config_models_knotless
  print('dict(body)', dict(body))
  for config_item in dict(body):
    if dict(body)[config_item] != None:
      new_config_item = config_models[config_item](**{config_item: dict(body)[config_item]})
      db.add(new_config_item)
      db.commit()
      db.refresh(new_config_item)
  return new_config_item

@router.delete('/{netType}/{type}/{id}')
def delete_config(netType: str, type: str, id: int, force: bool | None = None, db = Depends(database.get_session)):
  config_models = config_models_plastic if netType == 'plastic' else config_models_knotless
  net_model = NetPlastic if netType == 'plastic' else NetKnotless
  def nets_relate_with_config():
    print(netType)
    delete_element = db.query(config_models[type]).filter(config_models[type].id == id).first()
    existing_nets = db.query(net_model).filter(getattr(net_model, type) == delete_element.id).all()
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

