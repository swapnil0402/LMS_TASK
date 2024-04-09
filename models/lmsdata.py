from pydantic import BaseModel, Field, validator
from typing import Optional

class Address(BaseModel):
    city: str
    country: str

class Student(BaseModel):
    name: str
    age: int
    address: Address

    @validator("age")
    def age_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError("Age must be greater than 0")
        return value

    @validator("name")
    def name_length_must_be_at_least_three(cls, value):
        if len(value) < 3:
            raise ValueError("Name must contain at least 3 characters")
        return value

class PatchAddress(BaseModel):
    city: Optional[str] = None
    country: Optional[str] = None

class PatchStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    address: Optional[PatchAddress] = None

    @validator("age")
    def age_must_be_positive(cls, value):
        if value is not None and value <= 0:
            raise ValueError("Age must be greater than 0")
        return value

    @validator("name")
    def name_length_must_be_at_least_three(cls, value):
        if value is not None and len(value) < 3:
            raise ValueError("Name must contain at least 3 characters")
        return value
