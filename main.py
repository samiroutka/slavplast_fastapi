from fastapi import FastAPI, Depends
import database
from fastapi.middleware.cors import CORSMiddleware
import configs.configs_view as config
import nets.nets_view as nets

database.Base.metadata.create_all(bind = database.engine)

app = FastAPI()

app.include_router(config.router)
app.include_router(nets.router)

app.add_middleware(
  CORSMiddleware,
  allow_origins=['*'],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

