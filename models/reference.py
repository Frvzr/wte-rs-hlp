import uuid
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import UUID, String, Integer, ForeignKey

from config.database import Base


if TYPE_CHECKING:
    from ..models import Item


class SealType(Base):
    __tablename__ = "seal_types"

    name: Mapped[str] = mapped_column(String(25), unique=True)
    description: Mapped[str] = mapped_column(String(150), nullable=True)


class RedressLevel(Base):
    __tablename__ = "redress_levels"

    level: Mapped[str] = mapped_column(String(25), unique=True)
    description: Mapped[str] = mapped_column(String(150), nullable=True)

    kits: Mapped[list["Kit"]] = relationship(back_populates="redress_level")


class Category(Base):
    __tablename__ = "category"
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, nullable=False, default=uuid.uuid4, unique=True)
    name: Mapped[String] = mapped_column(String(32), nullable=False, unique=True)
    description: Mapped[String | None] = mapped_column(String(128), nullable=True)
    parent_category: Mapped[UUID | None] = mapped_column(UUID, ForeignKey("category.id"), nullable=True)

    item: Mapped['Equipment'] = relationship(
        'Equipment',
        primaryjoin='Equipment.category_id == Category.id',
        back_populates='category',
        foreign_keys='Equipment.category_id'
    )

    children: Mapped[list["Category"]] = relationship(back_populates="parent")
    parent: Mapped["Category"] = relationship(back_populates="children", remote_side=[id])


class Size(Base):
    __tablename__ = "size"
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, nullable=False, default=uuid.uuid4, unique=True)
    name: Mapped[String] = mapped_column(String(32), nullable=False)
    description: Mapped[String] = mapped_column(String(128), nullable=True)


class Type(Base):
    __tablename__ = "types"
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, nullable=False, default=uuid.uuid4, unique=True)
    name: Mapped[String] = mapped_column(String(32), nullable=False)
    description: Mapped[String] = mapped_column(String(128), nullable=True)
    is_active: Mapped[bool] = mapped_column(nullable=False, default=True)

    item: Mapped['Item'] = relationship(
        'Item',
        primaryjoin='Item.type_id == Type.id',
        back_populates='type',
        foreign_keys='Item.type_id'
    )
