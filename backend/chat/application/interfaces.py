from abc import abstractmethod, ABC
from dataclasses import dataclass
from typing import Optional
from entities import User, Chat


class UsersRepo(ABC):

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[User]:
        ...

    @abstractmethod
    def add(self, user: User):
        ...

    @abstractmethod
    def create(self, user: User):
        ...

    @abstractmethod
    def remove(self, id: int):
        ...


class AdminRepo(UsersRepo, ABC):
    pass


class ChatRepo(ABC):

    @abstractmethod
    def get_by_id(self, id: int):
        ...

    @abstractmethod
    def create(self, title: str, chat_owner: str):
        ...

    @abstractmethod
    def remove(self, id: int):
        ...

    @abstractmethod
    def send_message(self, id: int, text: str):
        ...


class MessageRepo(ABC):

    @abstractmethod
    def get_by_id(self, id: int):
        ...

    @abstractmethod
    def create(self, chat: Chat):
        ...

    @abstractmethod
    def remove(self, id: int):
        ...


# class UserChatRepo(ABC):
#
#     @abstractmethod
#     def get_by_chat(self, chat: Chat):
#         ...
#
#     @abstractmethod
#     def get_by_user(self, user: User):
#         ...
