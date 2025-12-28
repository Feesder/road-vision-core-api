from dataclasses import dataclass


@dataclass
class CreateUserDto:
    username: str
    email: str
    password: str


@dataclass
class UserDto:
    username: str
    email: str
