from classic.app import DTO, validate_with_dto
from classic.components import component
from backend.chat.adapters.storage import repositories
from backend.chat.application.entities import Chat, User


class MessageInfo(DTO):
    user_id: int
    text: str


class ChatInfo(DTO):
    user_id: int
    title: str


# @component
class ChatService:
    chat_repo = repositories.ChatRepo()

    def create_chat(self, title: str, chat_owner: int) -> Chat:
        return self.chat_repo.create(title, chat_owner)

    def get_chat_by_id(self, chat_id: int) -> Chat:
        return self.chat_repo.get_by_id(chat_id)

    def remove_chat(self, chat_id: int):
        self.chat_repo.remove(chat_id)

    def modify_chat_info(self, chat_id: int, title: str):
        self.chat_repo.modify_chat_info(chat_id, title)


@component
class UserService:
    user_repo: repositories.UsersRepo

    def create_user(self, name: str, phone: str):
        self.user_repo.create(name, phone)

    def get_user_by_id(self, user_id: int) -> dict:
        return self.user_repo.get_by_id(user_id)

    def remove_user(self, user_id: int):
        self.user_repo.remove(user_id)
