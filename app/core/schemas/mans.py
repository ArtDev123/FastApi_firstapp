from pydantic import BaseModel

from typing import List

class CategorySchema(BaseModel):
    cat_name: str
    mans: List["ManSchema"]

class ManSchema(BaseModel):
    first_name: str
    last_name: str
    description: str
    categories: List["CategorySchema"]