from fastapi import APIRouter, UploadFile, HTTPException
from fastapi.responses import FileResponse
import shutil, os

files_dir = 'media'

router = APIRouter(tags=['file'])

@router.get('/file/{filename}')
def get_file(filename: str):
  if filename in os.listdir(files_dir):
    return FileResponse(f'{files_dir}/{filename}')
  else:
    raise HTTPException(status_code=404, detail=f'there is no file with name: {filename}')

@router.post('/file')
def upload_file(file: UploadFile):
  if not os.path.isdir(files_dir):
    os.makedirs(files_dir)
  with open(f'{files_dir}/{file.filename}', 'wb') as buffet:
    shutil.copyfileobj(file.file, buffet)
  return f'file/{file.filename}'

@router.delete('/file/{filename}')
def get_file(filename: str):
  if filename in os.listdir(files_dir):
    os.remove(f'{files_dir}/{filename}')
    return True
  else:
    raise HTTPException(status_code=404, detail=f'there is no file with name: {filename}')