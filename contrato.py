from datetime import datetime
from typing import Tuple
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt, validate_call, validator
from enum import Enum

class ProdutoEnum (str, Enum):
    produto1 = "Produto 1"
    produto2 = "Produto 2"
    produto3 = "Produto 3"
    

class Vendas(BaseModel):
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum