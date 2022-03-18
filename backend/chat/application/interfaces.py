from abc import abstractmethod, ABC
from dataclasses import dataclass
from typing import Optional
from backend.chat.application.entities import Chat, User


class UsersRepo(ABC):

    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[User]:
        ...

    # @abstractmethod
    # def add(self, user: User):
    #     ...

    @abstractmethod
    def create(self, name: str, phone: str):
        ...

    @abstractmethod
    def remove(self, user_id: int):
        ...


class ChatRepo(ABC):

    @abstractmethod
    def get_by_id(self, chat_id: int):
        ...

    @abstractmethod
    def create(self, title: str, chat_owner: str):
        ...

    @abstractmethod
    def remove(self, chat_id: int):
        ...

    @abstractmethod
    def send_message(self, chat_id: int, text: str):
        ...


class MessageRepo(ABC):

    @abstractmethod
    def get_by_id(self, message_id: int):
        ...

    @abstractmethod
    def create(self, chat: Chat):
        ...

    @abstractmethod
    def remove(self, message_id: int):
        ...
