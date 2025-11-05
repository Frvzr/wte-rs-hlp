from typing import Optional
from pydantic import UUID4

from . import BaseSchema, TimestampSchema


class SealTypeBase(BaseSchema):
    name: str
    description: str | None = None


class SealTypeCreate(SealTypeBase):
    pass


class SealTypeUpdate(BaseSchema):
    name: str | None = None
    description: str | None = None


class SealTypeResponse(SealTypeBase, TimestampSchema):
    id: UUID4


class CategoryBase(BaseSchema):
    name: str
    description: str | None = None
    parent_category: UUID4 | None


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(BaseSchema):
    name: str | None = None
    description: str | None = None
    parent_category: UUID4 | None


class CategoryResponse(CategoryBase, TimestampSchema):
    id: UUID4
