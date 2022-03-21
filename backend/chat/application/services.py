from classic.components import component
from classic.app import DTO, validate_with_dto
from backend.chat.application.entities import Chat, User, Message
from backend.chat.application import interfaces
from . import errrors

from pydantic import validate_arguments
from typing import Optional, List


class ChatInfoDTO(DTO):
    chat_id: Optional[int]
    title: str
    user_id: int
    chat_owner: Optional[int]
    messages: Optional[List[int]]
    users: Optional[List[int]]


class MessageInfoDTO(DTO):
    chat_id: int
    message: str
    user_id: int


class UserInfoDTO(DTO):
    name: str
    phone: Optional[str]
    password: str


class UserInviteInfo(DTO):
    chat_id: int
    guest_id: int
    user_id: int


@component
class ChatService:
    chat_repo: interfaces.ChatRepo
    user_repo: interfaces.UserRepo
    message_repo: interfaces.MessageRepo

    def _is_chat_owner(self, chat_id: int, user_id: int):
        chat = self.get_chat_by_id(chat_id)
        user = self.get_user_by_id(user_id)
        if user.id == chat.chat_owner:
            return True
        else:
            raise errrors.NoRightsError

    def _is_chat_member(self, chat_id: int, user_id: int):
        chat = self.get_chat_by_id(chat_id)
        user = self.get_user_by_id(user_id)
        print(chat)
        if chat.users:
            if user.id in chat.users or user.id == chat.chat_owner:
                return True
        elif user.id == chat.chat_owner:
            print('we are here')
            return True
        else:
            raise errrors.NoRightsError

    @validate_with_dto
    def create_chat(self, chat_info: ChatInfoDTO) -> Chat:
        return self.chat_repo.create_chat(chat_info.title, chat_info.user_id)

    @validate_arguments
    def get_chat_by_id(self, chat_id: int) -> Optional[Chat]:
        chat = self.chat_repo.get_by_id(chat_id)
        if chat:
            return chat
        else:
            raise errrors.ChatNotFound

    @validate_arguments
    def get_chat_info(self, chat_id: int, user_id: int):
        chat = self.chat_repo.get_by_id(chat_id)
        if self._is_chat_member(chat_id, user_id):
            return chat

    @validate_arguments
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        user = self.user_repo.get_by_id(user_id)
        if user:
            return user
        else:
            raise errrors.UserNotFound

    @validate_with_dto
    def update_chat_info(self, chat_info: ChatInfoDTO) -> Optional[Chat]:
        if self._is_chat_owner(chat_info.chat_id, chat_info.user_id):
            return self.chat_repo.update_chat_info(chat_info.chat_id, chat_info.title)
        else:
            raise errrors.NoRightsError

    @validate_with_dto
    def send_message(self, message_info: MessageInfoDTO) -> Optional[Message]:
        if self._is_chat_member(message_info.chat_id, message_info.user_id):
            message = self.message_repo.create(message_info.user_id, message_info.message)
            # chat = self.chat_repo.get_by_id(message_info.chat_id)
            self.chat_repo.add_message(message_info.chat_id, message.id)
            return message

    @validate_arguments
    def get_all_users(self, chat_id: int, user_id: int) -> Optional[List[dict]]:
        print(chat_id, user_id)
        if self._is_chat_member(chat_id, user_id):
            return self.chat_repo.get_all_users(chat_id)

    @validate_arguments
    def get_all_messages(self, chat_id: int, user_id: int) -> Optional[List[dict]]:
        if self._is_chat_member(chat_id, user_id):
            return self.chat_repo.get_all_messages(chat_id)
        else:
            raise errrors.NoRightsError

    @validate_arguments
    def remove_chat(self, chat_id: int, user_id: int):
        if self._is_chat_owner(chat_id, user_id):
            self.chat_repo.remove(chat_id)

    @validate_with_dto
    def invite_user(self, invite_info: UserInviteInfo):
        guest = self.get_user_by_id(invite_info.guest_id)
        if self._is_chat_owner(invite_info.chat_id, invite_info.user_id):
            self.chat_repo.add_user(invite_info.chat_id, invite_info.guest_id)
        else:
            raise errrors.NotOwnerError


@component
class UserService:
    user_repo: interfaces.UserRepo

    @validate_with_dto
    def create_user(self, user_info: UserInfoDTO):
        return self.user_repo.create(user_info.name, user_info.phone, user_info.password)

    @validate_with_dto
    def login(self, user_info: UserInfoDTO) -> str:
        return self.user_repo.login(user_info.name, user_info.password)
