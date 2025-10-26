from src.apps.accounts.models import User
from src.apps.accounts.repository import UserRepository, user_repo
from src.utils.services import AbstractService


class UserService(AbstractService[User]):
    def __init__(self, repository: UserRepository = user_repo):
        super().__init__(repository)


user_service = UserService()
