from pydantic import UUID4

from . import BaseSchema, TimestampSchema


class ItemBase(BaseSchema):
    part_number: str
    description: str | None = None
    category_id: UUID4 | None = None
    group_id: UUID4 | None = None
    source_id: UUID4 | None = None
    operation_id: UUID4 | None = None
    department_id: UUID4 | None = None
    type_id: UUID4 | None = None
    unit_id: UUID4 | None = None
    is_active: bool = True


class ItemCreate(ItemBase):
    pass


class ItemUpdate(BaseSchema):
    part_number: str | None
    description: str | None = None
    category_id: UUID4 | None = None
    group_id: UUID4 | None = None
    source_id: UUID4 | None = None
    operation_id: UUID4 | None = None
    department_id: UUID4 | None = None
    type_id: UUID4 | None = None
    unit_id: UUID4 | None = None
    is_active: bool = True


class ItemResponse(ItemBase, TimestampSchema):
    id: UUID4
