from pydantic import BaseModel
from typing import Optional,List


class Products(BaseModel):
    productName: str
    description: str
    amount: int
    rating: float
    productImage: str

class ResponseModel(BaseModel):
    productName: str
    description: str
    amount: int
    rating: float
    productImage: str

class ResponseList(BaseModel):
    data:Optional[List[ResponseModel]]    
