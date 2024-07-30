from fastapi import FastAPI, Depends
import database
from fastapi.middleware.cors import CORSMiddleware
import configs.configs_view as config
import nets.nets_view as nets
import files.files_view as files
import password.password_view as password

database.Base.metadata.create_all(bind = database.engine)

app = FastAPI()

app.include_router(config.router)
app.include_router(nets.router)
app.include_router(files.router)
app.include_router(password.router)

app.add_middleware(
  CORSMiddleware,
  allow_origins=['*'],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

