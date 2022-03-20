import pytest
from pydantic import ValidationError

from backend.chat.application.services import ChatService


@pytest.fixture(scope='function')
def service(chat_repo, user_repo, message_repo):
    return ChatService(chat_repo=chat_repo, user_repo=user_repo, message_repo=message_repo)


def test__create_chat(service, chat_repo):
    new_chat = {
        'chat_id': 1,
        'user_id': 1,
        'title': 'New Chat'
    }
    assert service.create_chat(**new_chat) == chat_repo.create_chat()

