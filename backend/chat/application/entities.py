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
    id: int
    user: User
    chat: 'Chat'
    message: str


# @dataclass
# class BannedUser:
#     user: User
#     chat: Chat


# @dataclass
# class UserChat:
#     chat: 'Chat'
#     user: List[User]


@dataclass
class Chat:
    id: int
    title: str
    admin: User
    users: List[User] = None
    # banned: List[User] = None

    def add_user(self, user: User):
        if user not in self.users:
            self.users.append(user)

    def remove_user(self, user: User):
        if user in self.users:
            self.users.remove(user)

    def modify_chat_info(self, title: str):
        self.title = title
