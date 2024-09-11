from datetime import datetime
from typing import Tuple
from pydantic import BaseModel, EmailStr, validade_call
from enum import Enum

class ProdutoEnum (str, Enum):
    produto1 = "Zapflow com Gemini"
    produto2 = "Zapflow com ChatGPT"
    produto3 = "Zapflow com Lhama"
    

class Vendas(BaseModel):
    email: EmailStr
    data: datetime
    valor: float    
    quantidade: int
    produto: ProdutoEnum
    
    @validade_call('produto')
    def categoria_no_enum(cls, v):
        return v
