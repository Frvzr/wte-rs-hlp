from typing import List, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from models import Item, RedressKitConsist, Category
from repositories.base import BaseRepository


class RedressKitRepository(BaseRepository[Item]):
    def __init__(self, session: AsyncSession):
        super().__init__(session, Item)

    async def get_with_items_by_id(self, redress_kit_id: str) -> Optional[Item]:
        pass
