
from fastapi import APIRouter

router = APIRouter(tags=['password'])

password = 'slavplast'

@router.get('/password')
def get_password():
  return password
