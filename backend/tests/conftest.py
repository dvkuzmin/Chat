import pytest

from backend.chat.application import entities


@pytest.fixture(scope='function')
def user():
    return entities.User(
        id=1,
        name='vasya',
        phone='911',
        password='qwerty',
        token=None,
    )


@pytest.fixture(scope='function')
def message():
    return entities.Message(
        id=1,
        user=1,
        message='Hello'
    )


@pytest.fixture(scope='function')
def chat():
    return entities.Chat(
        id=1,
        title='flood',
        chat_owner=1,
        messages=[1],
        users=[1]
    )
