from pydantic import EmailStr
from src.utils.dto import BaseDTO

class UserDTO(BaseDTO):
    username: str
    email: EmailStr
    password: str


class UserRegisterDTO(UserDTO):
    email: EmailStr