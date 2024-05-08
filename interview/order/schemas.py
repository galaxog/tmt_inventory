from decimal import Decimal
from pydantic import BaseModel


class OrderIsActiveData(BaseModel):

    id: int
    is_active: bool
