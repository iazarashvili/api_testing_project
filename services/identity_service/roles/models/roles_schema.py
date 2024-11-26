from typing import List, Optional

from pydantic import BaseModel, field_validator, validator


class Roles(BaseModel):
    id: str
    name: str
    normalizedName: str
    concurrencyStamp: str

    @field_validator('id', 'name', 'normalizedName', 'concurrencyStamp')
    def fields_are_not_empty(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value


class RolesSchema(BaseModel):
    data: List[Roles]

    @field_validator('data')
    def check_roles(cls, value):
        if 16 > len(value) > 17:
            raise ValueError('the length is not 20')
        else:
            return value
