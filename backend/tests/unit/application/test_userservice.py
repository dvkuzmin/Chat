import pytest
from pydantic import ValidationError

from backend.chat.application.services import UserService


@pytest.fixture(scope='function')
def service(user_repo):
    return UserService(user_repo=user_repo)


def test__create_user(service, user_repo):
    new_user = {
        'name': 'vasya',
        'phone': '911',
        'password': 'qwerty'
    }

    assert service.create_user(**new_user) == user_repo.create()


def test__create_user_bad(service):
    new_user = {
        'name': 'vasya',
        'phone': '911'
    }

    with pytest.raises(ValidationError):
        service.create_user(**new_user)
