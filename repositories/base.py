from typing import Optional, List, TypeVar, Generic, Type
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from config.database import Base

T = TypeVar('T', bound=Base)


class BaseRepository(Generic[T]):
    pass
