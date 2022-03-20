from abc import abstractmethod, ABC
from dataclasses import dataclass
from typing import Optional, List
from backend.chat.application.entities import Chat, User, Message


class UserRepo(ABC):

    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[User]:
        ...

    @abstractmethod
    def create(self, name: str, phone: str, password: str):
        ...

    @abstractmethod
    def login(self, name: str, password: str) -> str:
        ...


class ChatRepo(ABC):

    @abstractmethod
    def get_by_id(self, chat_id: int) -> Optional[Chat]:
        ...

    @abstractmethod
    def create_chat(self, title: str, chat_owner: int) -> Chat:
        ...

    @abstractmethod
    def remove(self, chat_id: int):
        ...

    @abstractmethod
    def update_chat_info(self, chat_id: int, title: str) -> Optional[Chat]:
        ...

    @abstractmethod
    def get_all_users(self, chat_id: int):
        ...

    @abstractmethod
    def get_all_messages(self, chat_id: int):
        ...

    @abstractmethod
    def add_user(self, chat_id: int, user_id: int):
        ...

    @abstractmethod
    def add_message(self, chat_id: int, user_id: int):
        ...


class MessageRepo(ABC):

    @abstractmethod
    def create(self, user_id: int, message: str) -> Message:
        ...

