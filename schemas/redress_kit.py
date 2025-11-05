from pydantic import UUID4

from .item import ItemShortDetail
from . import BaseSchema, TimestampSchema


class RedressKitConsistBase(BaseSchema):
    redress_kit_id: UUID4
    item_id: UUID4
    quantity: float
    revision: str


# v.1
class RedressKitConsistDetailV1(BaseSchema):
    redress_kit: str
    description_redress_kit: str | None = None
    item: str
    description_item: str | None = None
    quantity: float
    revision: str


# v.2
class RedressKitConsistDetailV2(BaseSchema):
    redress_kit: ItemShortDetail
    redress_kit: list[ItemShortDetail]
    quantity: float
    revision: str


class RedressKitConsistCreate(RedressKitConsistBase):
    pass


class RedressKitConsistUpdate(BaseSchema):
    redress_kit_id: UUID4 | None = None
    item_id: UUID4 | None = None
    quantity: float | None = None
    revision: str | None = None
