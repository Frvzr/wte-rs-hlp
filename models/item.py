import uuid

from typing import TYPE_CHECKING

from sqlalchemy import String, Text, UUID, ForeignKey, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship

from config.database import Base

if TYPE_CHECKING:
    from ..models import RedressKitConsist, Category, Asset


class Item(Base):
    __tablename__ = "equipment"

    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, nullable=False, default=uuid.uuid4, unique=True)
    part_number: Mapped[String] = mapped_column(String(32), nullable=False, unique=True)
    description: Mapped[Text] = mapped_column(String(128), nullable=True)
    category_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('category.id'), nullable=True, unique=False)
    group_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('groups.id'), nullable=True, unique=False)
    source_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('sources.id'), nullable=True, unique=False)
    operation_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('operations.id'), nullable=True, unique=False)
    department_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('departments.id'), nullable=True, unique=False)
    type_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('types.id'), nullable=True, unique=False)
    unit_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('units.id'), nullable=True, unique=False)
    is_active: Mapped[bool] = mapped_column(nullable=False, default=True)

    redress_kit_consist: Mapped[list['RedressKitConsist']] = relationship(
        'RedressKitConsist',
        primaryjoin='Item.id == RedressKitConsist.item_id',
        back_populates='item',
        foreign_keys='RedressKitConsist.item_id'
    )

    category: Mapped['Category'] = relationship(
        'Category',
        primaryjoin='Item.category_id == Category.id',
        back_populates='item',
        foreign_keys='Item.category_id'
    )

    redress_kit: Mapped[list['Item']] = relationship(
        'RedressKitConsist',
        primaryjoin='RedressKitConsist.redress_kit_id == Item.id',
        back_populates='redress_kit',
        foreign_keys='RedressKitConsist.redress_kit_id'
    )

    asset: Mapped['Asset'] = relationship(
        'Asset',
        primaryjoin='Item.id == Asset.equipment_id',
        back_populates='equipment',
        foreign_keys='Asset.equipment_id'
    )

    type: Mapped['Type'] = relationship(
        'Type',
        primaryjoin='Item.type_id == Type.id',
        back_populates='item',
        foreign_keys='Item.type_id'
    )

    unit: Mapped['Unit'] = relationship(
        'Unit',
        primaryjoin='Item.unit_id == Unit.id',
        back_populates='item',
        foreign_keys='Item.unit_id'
    )

    __table_args__ = (
        Index('ix_items_is_active', 'is_active'),
    )

