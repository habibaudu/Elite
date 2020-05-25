import pytest
from mixer.backend.django import mixer
from users_app.models import User


@pytest.fixture(scope='function')
def new_user():
    return {
        "first_name": "over",
        "last_name": "drive",
        "email": "drive@gmail.com",
        "password": "Hb1234Qw"
    }

@pytest.fixture()
def new_valid_user():
    new_user = {
        "first_name": "over",
        "last_name": "drive",
        "email": "drive@gmail.com",
        "password": "Hb1234Qw"
    }
    new_user['is_active'] = True
    user = mixer.blend(User, **new_user)
    new_user['id'] = user.id
    return new_user


@mixer.middleware(User)
def password_encription(user):
    user.set_password('Hb1234Qw')
    return user

