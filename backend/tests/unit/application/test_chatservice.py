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


def test_create_chat_bad(service, chat_repo):
    new_chat = {
        'chat_id': 1,
        'user_id': 1
    }
    with pytest.raises(ValidationError):
        assert service.create_chat(**new_chat)


def test_send_message(service, message_repo):
    new_message = {
        "chat_id": 1,
        "message": "Hi",
        "user_id": 1,
    }
    assert service.send_message(**new_message) == message_repo.create()


def test_send_message_bad(service):
    new_message = {
        "message": "Hi",
        "user_id": 1,
    }
    with pytest.raises(ValidationError):
        service.send_message(**new_message)


def test_get_chat_info(service, chat_repo):
    data = {
        "chat_id": 1,
        "user_id": 1
    }
    assert service.get_chat_info(**data) == chat_repo.get_by_id()


def test_get_chat_info_bad(service, chat_repo):
    data = {
        "chat_id": 1
    }
    with pytest.raises(ValidationError):
        service.get_chat_info(**data)


def test_update_chat_info(service, chat_repo):
    data = {
        "chat_id": 1,
        "user_id": 1,
        "title": "New chat"
    }
    assert service.update_chat_info(**data) == chat_repo.update_chat_info()


def test_update_chat_info_bad(service):
    data = {
        "chat_id": 1,
        "title": "New chat"
    }
    with pytest.raises(ValidationError):
        service.update_chat_info(**data)


def test_get_all_users(service, chat_repo):
    data = {
        "chat_id": 1,
        "user_id": 1
    }
    assert service.get_all_users(**data) == chat_repo.get_all_users()


def test_get_all_users_bad(service):
    data = {
        "chat_id": 1
    }
    with pytest.raises(ValidationError):
        assert service.get_all_users(**data)


def test_get_all_messages(service, chat_repo):
    data = {
        "chat_id": 1,
        "user_id": 1
    }
    assert service.get_all_messages(**data) == chat_repo.get_all_messages()


def test_get_all_messages_bad(service):
    data = {
        "chat_id": 1
    }
    with pytest.raises(ValidationError):
        assert service.get_all_messages(**data)


def test_remove_chat(service, chat_repo):
    data = {
        "chat_id": 1,
        "user_id": 1
    }
    assert service.remove_chat(**data) == chat_repo.remove()


def test_remove_chat_bad(service):
    data = {
        "chat_id": 1
    }
    with pytest.raises(ValidationError):
        assert service.remove_chat(**data)
