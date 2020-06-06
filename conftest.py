import pytest
from mixer.backend.django import mixer
from users_app.models import (User, Invent, State)
from network.models import (Connection)
from utils.enumerators import (RequestStatus)


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

@pytest.fixture()
def auth_header(client, new_valid_user):
    response = client.post('/api/v1/login',
                            data={
                                'email':new_valid_user['email'],
                                'password': new_valid_user['password']
                            })
    token = str(response.data["token"],'utf-8')
    header = {"HTTP_AUTHORIZATION": 'Bearer ' + token}
    return header

@pytest.fixture()
def new_state():
    state = {
        "state": "plateau",
        "capital":"jos",
        "created_at": "2019-11-24T23:09:34.713380Z",
        "updated_at": "2019-11-24T23:09:34.713380Z"
    }
    state_instance = mixer.blend(State, **state)
    state['id'] = state_instance.id
    return state
    
@pytest.fixture()
def invention_data(new_state):
    return {
	       "location":new_state['id'],
	       "title":"my invention",
	       "invent_media":"https://www.inghrtud.commm/imahe.png",
	       "about_invention":"Its the coollest invention in the history of inventions yes yes"
            }

@pytest.fixture
def new_valid_user2():
    new_user2 = {
        "first_name": "over2",
        "last_name": "drive2",
        "email": "drive2@gmail.com",
        "password": "Hb1234Qw"
    }
    new_user2['is_active'] = True
    user2 = mixer.blend(User,**new_user2)
    new_user2['id'] = user2.id

    return new_user2

@pytest.fixture()
def connection(new_valid_user2):
    return {
        "target_user":new_valid_user2['id']
    }

@pytest.fixture()
def new_connection(new_valid_user2,new_valid_user):
    connection = {
        "initiator_id":new_valid_user2['id'],
        "following_id":new_valid_user['id'],
        "request":RequestStatus.pending.value,
        "created_at": "2019-11-24T23:09:34.713380Z",
        "updated_at": "2019-11-24T23:09:34.713380Z"
    }
    conn = mixer.blend(Connection,**connection)
    connection['id']= conn.id
    return connection

@pytest.fixture()
def connection_two(new_valid_user):
    return{
        "target_user":new_valid_user['id']
    }