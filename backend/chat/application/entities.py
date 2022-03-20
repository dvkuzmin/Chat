from dataclasses import dataclass
from typing import List, Optional
import datetime


@dataclass
class User:
    id: int
    name: str
    phone: str
    password: str
    token: Optional[str] = None


@dataclass
class Message:
    id: int
    user: int
    message: str
    # date_created: datetime.datetime


@dataclass
class Chat:
    id: int
    title: str
    chat_owner: int
    messages: Optional[List[int]] = None
    users: Optional[List[int]] = None

    def add_user(self, user_id: int):
        if user_id not in self.users:
            self.users.append(user_id)

    def remove_user(self, user_id: int):
        if user_id in self.users:
            self.users.remove(user_id)

    def modify_chat_info(self, title: str):
        self.title = title

    def add_message(self, message_id: int):
        if self.messages:
            self.messages.append(message_id)
        else:
            self.messages = [message_id]
