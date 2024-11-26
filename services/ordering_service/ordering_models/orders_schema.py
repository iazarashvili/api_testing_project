from pydantic import BaseModel


class OrdersSchema(BaseModel):
    externalId: int
    id: str

