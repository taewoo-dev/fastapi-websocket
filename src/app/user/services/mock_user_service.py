import random
import string

from fastapi import Depends

from app.user.models.user import User
from app.user.repositorys.user_repository import UserRepository


class MockUserService:
    def __init__(
        self,
        repo: UserRepository = Depends(),
    ):
        self.user_repo = repo

    async def generate_random_user(self):
        user_name = "User" + "".join(
            random.choices(string.ascii_letters, k=5)
        )  # 랜덤한 5글자 문자열 생성
        new_user = User.create(name=user_name)
        await self._create_user(user=new_user)
        return new_user.id, new_user.name

    async def _create_user(self, user: User):
        await self.user_repo.save(user=user)
