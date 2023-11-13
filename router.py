from fastapi import APIRouter, Query
from app.query_parameter import read_items
from app.query_parameter import optional_parameter
from app.query_parameter import query_paramter_type_conversion
from app.query_parameter import multiple_path_and_query_parameters
from app.query_parameter import required_query_parameters
from app.request_body import create_item
from model.item import Item
from typing import Annotated

router = APIRouter()

@router.get("/")
def root():
  return {"hello": "world"}

# query_parameter 
@router.get("/items/", tags=["Query Parameter"])
async def read_item(skip: int = 0, limit: int = 10):
  return read_items(skip, limit)

@router.get("/items/{item_id}", tags=["Query Parameter"])
def read_item(item_id: str, q: str | None = None):
  return optional_parameter(item_id, q)

@router.get("/items/type-conversion/{item_id}", tags=["Query Parameter"])
async def read_item(item_id: str, q: str | None = None, short: bool = False):
  return query_paramter_type_conversion(item_id, q, short)

@router.get("/users/{user_id}/items/{item_id}", tags=["Query Parameter"])
async def read_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
  return multiple_path_and_query_parameters(user_id, item_id, q, short)

@router.get("/items/required/{item_id}", tags=["Query Parameter"])
async def read_user_item(item_id: str, needy: str):
  return required_query_parameters(item_id, needy)

# request_body
@router.post("/items/", tags=["Request Body"])
async def create_item(item: Item):
  return item


# query parameter & string validation
# @router.get("/items/", tags=["Query Parameter and String Validation"])
# def read_items(q: Annotated[str | None, Query(max_length=50)]):
#   results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#   if q:
#       results.update({"q": q})
#   return results