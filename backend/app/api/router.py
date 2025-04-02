import json
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.schemas import SPartner, SMessge
from app.api.utils import (
    send_msg,
    create_new_room,
    get_user_info,
    get_all_rooms_gender,
    add_user_to_room,
    refund_partner,
    is_match,
)
from app.dao.fastapi_dao_dep import get_session_without_commit
from app.redis_dao.custom_redis import CustomRedis
from app.redis_dao.manager import get_redis

router = APIRouter(prefix="/api", tags=["АПИ"])

