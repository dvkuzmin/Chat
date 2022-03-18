from typing import Optional
from . import storage
from dataclasses import asdict

from backend.chat.application import interfaces
from backend.chat.application.entities import User, Message, Chat


class UsersRepo(interfaces.UsersRepo):

    def get_by_id(self, user_id: int) -> Optional[dict]:
        return storage.users.get(user_id)

    def create(self, name: str, phone: str) -> User:
        user_id = len(storage.users) + 1
        user = User(user_id, name, phone)
        return user

    def remove(self, user_id: int):
        if user_id in storage.users:
            del storage.users[user_id]
            for id_ in range(user_id+1, len(storage.users)+1):
                storage.users[id_] = id_ - 1


class ChatRepo(interfaces.ChatRepo):

    def get_by_id(self, chat_id: int) -> Optional[Chat]:
        data = storage.chats.get(chat_id)
        if data:
            title = data.get('title')
            admin = data.get('admin')
            users = data.get('users')
            chat = Chat(chat_id, title, admin, users)
            return chat

    def create(self, title: str, chat_owner: int) -> Chat:
        chat_id = len(storage.chats) + 1
        chat = Chat(chat_id, title, storage.users[chat_owner])
        storage.chats[chat.id] = asdict(chat)
        del storage.chats[chat.id]['id']
        return chat

    def remove(self, chat_id: int):
        if chat_id in storage.chats:
            del storage.chats[chat_id]
            for id_ in range(chat_id+1, len(storage.chats+1)):
                storage.chats[id_] = id_ - 1

    def send_message(self, chat_id: int, text: str):
        pass

    def modify_chat_info(self, chat_id: int, title: str):
        if chat_id in storage.chats:
            storage.chats['title'] = title


class MessageRepo(interfaces.MessageRepo):

    def get_by_id(self, message_id: int) -> Optional[Message]:
        pass

    def create(self, chat: Chat):
        pass

    def remove(self, message_id: int):
        pass
