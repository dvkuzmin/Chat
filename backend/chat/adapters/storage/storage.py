from backend.chat.application.entities import User, Chat, Message
from dataclasses import asdict, dataclass
from pprint import pprint
from typing import Any, Iterable

SECRET = "DFSDDF2345msf23asdfs"

# Добавляем какие то фикстуры для тестирования
#
# user_1 = User(1, 'Vasya', '911')
# user_2 = User(2, 'Vanya', '01')
# user_3 = User(3, 'Petya', '02')
# user_4 = User(4, 'Kolya', '03')
#
#
# message_1 = Message(1, user_1.id, 'hello')
# message_2 = Message(2, user_2.id, 'hi')
# message_3 = Message(3, user_3.id, 'hey there')
#
# chat_1 = Chat(1, 'spam', user_1.id, [message_1.id, message_2.id], [user_3.id, user_2.id])
# chat_2 = Chat(2, 'work', user_4.id, [message_2.id, message_3.id], [user_2.id, user_4.id, user_3.id])
#
# users = [user_1, user_2, user_3, user_4]
# chats = [chat_1, chat_2]
# messages = [message_1, message_2, message_3]
#
#
# def add_to_storage(storage: Iterable):
#     res = {}
#     for el in storage:
#         data = asdict(el)
#         res[data.pop('id')] = data
#     return res
#
#
# users = add_to_storage(users)
# chats = add_to_storage(chats)
# messages = add_to_storage(messages)

users = {}
chats = {}
messages = {}
# pprint(messages)
# pprint(chats)
