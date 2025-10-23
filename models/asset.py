import uuid
from typing import TYPE_CHECKING

from sqlalchemy import String, UUID, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from config.database import Base

if TYPE_CHECKING:
    from ..models import Item, RedressEquipment


class Asset(Base):
    __tablename__ = "assets"
    id: Mapped[UUID] = mapped_column(UUID, primary_key=True, nullable=False, default=uuid.uuid4, unique=True)
    serial_number: Mapped[String] = mapped_column(String(32), nullable=False, unique=True)
    equipment_id: Mapped[UUID] = mapped_column(UUID, ForeignKey('items.id'), nullable=False, unique=False)
    is_active: Mapped[bool] = mapped_column(default=True)
    status: Mapped[UUID] = mapped_column(UUID, ForeignKey('statuses.id'), nullable=True, unique=False)

    equipment: Mapped['Item'] = relationship(
        'Item',
        primaryjoin='Item.id == Asset.equipment_id',
        back_populates='asset',
        foreign_keys='Asset.equipment_id'
    )

    main_asset: Mapped[list['RedressEquipment']] = relationship(
        'RedressEquipment',
        primaryjoin='Asset.id == RedressEquipment.asset_id',
        back_populates='sn',
        foreign_keys='RedressEquipment.asset_id'
    )

    top_level: Mapped[list['RedressEquipment']] = relationship(
        'RedressEquipment',
        primaryjoin='Asset.id == RedressEquipment.top_tool',
        back_populates='top',
        foreign_keys='RedressEquipment.top_tool'
    )

    __table_args__ = {
        "comment": "Таблица с оборудованием"
    }
