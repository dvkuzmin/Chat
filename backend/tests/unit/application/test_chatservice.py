import pytest
from pydantic import ValidationError

from backend.chat.application.services import ChatService


@pytest.fixture(scope='function')
def service(chat_repo, user_repo, message_repo):
    return ChatService(chat_repo=chat_repo, user_repo=user_repo, message_repo=message_repo)


def test_create_chat(service, chat_repo):
    new_chat = {
        'chat_id': 1,
        'user_id': 1,
        'title': 'New Chat'
    }
    assert service.create_chat(**new_chat) == chat_repo.create_chat()


def test_send_message(service, chat_repo, message_repo):
    new_message = {
        "chat_id": 1,
        "message": "Hi",
        "user_id": 1,
    }
    assert service.send_message(**new_message) == message_repo.create()


def test_get_chat_info(service, chat_repo):
    data = {
        "chat_id": 1,
        "user_id": 1
    }
    assert service.get_chat_info(**data) == chat_repo.get_by_id()
