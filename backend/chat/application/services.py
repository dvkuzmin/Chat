from datetime import datetime
from classic.app import DTO, validate_with_dto
from classic.components import component
import interfaces
from entities import Chat


class MessageInfo(DTO):
    user_id: int
    text: str
    # date_published: datetime.now()


class ChatInfo(DTO):
    user_id: int
    title: str
    # date_created: datetime.now()


@component
class ChatService:
    chat_repo: interfaces.ChatRepo

    def create_chat(self, title: str, chat_owner: str) -> None:
        self.chat_repo.create(title, chat_owner)

    def get_chat_by_id(self, chat_id: int) -> Chat:
        return self.chat_repo.get_by_id(chat_id)

    def remove_chat(self, chat_id: int):
        self.chat_repo.remove(chat_id)


@component
class UserService:
    pass