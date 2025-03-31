# Дочерний класс от base.py, который позволяет расширять методы класса base.py

from app.dao.base import BaseDAO
from app.dao.models import User

class UserDAO(BaseDAO[User]):
    model = User