from unittest.mock import Mock

import pytest

from backend.chat.application import interfaces


@pytest.fixture(scope='function')
def user_repo(user):
    user_repo = Mock(interfaces.UserRepo)
    user_repo.create = Mock(return_value=None)
    user_repo.login = Mock(return_value=None)
    user_repo.get_by_id = Mock(return_value=user)

    return user_repo


@pytest.fixture(scope='function')
def chat_repo(chat, user):
    chat_repo = Mock(interfaces.ChatRepo)
    chat_repo.get_by_id = Mock(return_value=chat)
    chat_repo.create_chat = Mock(return_value=None)
    chat_repo.remove = Mock(return_value=None)
    chat_repo.update_chat_info = Mock(return_value=chat)
    chat_repo.get_all_users = Mock(return_value=[user])
    chat_repo.add_message = Mock(return_value=None)

    return chat_repo


@pytest.fixture(scope='function')
def message_repo(message):
    message_repo = Mock(interfaces.MessageRepo)
    message_repo.create = Mock(return_value=message)

    return message_repo
