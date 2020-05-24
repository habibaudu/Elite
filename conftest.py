import pytest
from mixer.backend.django import mixer


@pytest.fixture(scope='function')
def new_user():
    return {
        "first_name": "john",
        "last_name": "doe",
        "email": "doe@gmail.com",
        "password": "Htt66aq1"
    }
