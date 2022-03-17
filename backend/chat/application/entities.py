from dataclasses import dataclass
from typing import List, Optional


@dataclass
class User:
    id: int
    name: str
    phone: str
    jwt: Optional[str] = None


@dataclass
class Message:
    id: str
    user: User
    chat: 'Chat'
    message: str

#
# @dataclass
# class BannedUser:
#     user: User
#     chat: Chat


@dataclass
class UserChat:
    user: User
    chat: 'Chat'


@dataclass
class Chat:

    id: int
    title: str
    admin: User
    users: List[User]
    # banned: List[User] = None

    def add_user(self, user: User):
        if user not in self.users:
            self.users.append(user)

    def remove_user(self, user):
        if user in self.users:
            self.users.remove(user)
