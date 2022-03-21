from typing import Optional, List
from dataclasses import asdict
import hashlib
import jwt


from . import storage
from backend.chat.application import interfaces
from backend.chat.application.entities import User, Message, Chat


class ChatRepo(interfaces.ChatRepo):

    def get_by_id(self, chat_id: int) -> Optional[Chat]:
        data = storage.chats.get(chat_id)
        if data:
            title = data.get('title')
            admin = data.get('chat_owner')
            users = data.get('users')
            messages = data.get('messages')
            chat = Chat(chat_id, title, admin, messages, users)
            return chat

    def create_chat(self, title: str, chat_owner: int) -> Chat:
        chat_id = len(storage.chats) + 1
        chat = Chat(chat_id, title, chat_owner)
        storage.chats[chat.id] = asdict(chat)
        del storage.chats[chat.id]['id']
        return chat

    def remove(self, chat_id: int) -> None:
        if chat_id in storage.chats:
            del storage.chats[chat_id]
            for id_ in range(chat_id+1, len(storage.chats)+1):
                storage.chats[id_] = id_ - 1

    def update_chat_info(self, chat_id: int, title: str) -> Optional[Chat]:
        storage.chats[chat_id]['title'] = title
        return self.get_by_id(chat_id)

    def get_all_users(self, chat_id: int) -> Optional[List[dict]]:
        chat = self.get_by_id(chat_id)
        if chat:
            all_users = []
            user_fields = {}
            users_ids = chat.users
            if users_ids:
                for user_id in users_ids:
                    user = storage.users[user_id]
                    user_fields.update(user)
                    if user_fields['token']:
                        user_fields.pop('token')
                    user_fields.pop('password')
                    all_users.append(user_fields)
                return all_users
            else:
                return [{f'{chat_id = }': "No users in chat"}]

    def get_all_messages(self, chat_id: int) -> Optional[List[dict]]:
        chat = self.get_by_id(chat_id)
        if chat:
            messages = []
            messages_ids = chat.messages
            if messages_ids:
                for message_id in messages_ids:
                    message = storage.messages[message_id]
                    messages.append(message)
                return messages
            else:
                return [{f'{chat_id = }': 'no messages in chat'}]

    def add_user(self, chat_id: int, user_id: int):
        if storage.chats[chat_id]['users']:
            storage.chats[chat_id]['users'].append(user_id)
        else:
            storage.chats[chat_id]['users'] = [user_id]

    def add_message(self, chat_id: int, message_id: int):
        if storage.chats[chat_id]['messages']:
            storage.chats[chat_id]['messages'].append(message_id)
        else:
            storage.chats[chat_id]['messages'] = [message_id]


class MessageRepo(interfaces.MessageRepo):

    def create(self, user_id: int, message: str) -> Message:
        if storage.messages:
            message_id = len(storage.messages) + 1
        else:
            message_id = 1
        message = Message(message_id, user_id, message)
        storage.messages[message.id] = asdict(message)
        del storage.messages[message.id]['id']
        return message


class UserRepo(interfaces.UserRepo):

    def get_by_id(self, user_id: int) -> Optional[User]:
        data = storage.users.get(user_id)
        if data:
            name = data.get('name')
            phone = data.get('phone')
            jwt = data.get('jwt')
            user = User(user_id, name, phone, jwt)
            return user

    def create(self, name: str, phone: str, password: str) -> User:
        if storage.users:
            user_id = len(storage.users) + 1
        else:
            user_id = 1
        password = hashlib.sha256(password.encode()).hexdigest()
        user = User(user_id, name, phone, password)
        storage.users[user.id] = asdict(user)
        del storage.users[user.id]['id']
        return user

    def login(self, name: str, password: str) -> str:
        for user_id in storage.users:
            if storage.users[user_id]['name'] == name and storage.users[user_id]['password'] == \
                    hashlib.sha256(password.encode()).hexdigest():
                if not storage.users[user_id]['token']:
                    token = jwt.encode({"user_id": user_id}, storage.SECRET, algorithm="HS256")
                    storage.users[user_id]['token'] = token
                else:
                    token = storage.users[user_id]['token']
                return token

