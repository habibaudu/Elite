import pytest

@pytest.mark.django_db
class TestLogin():
    url ='/api/v1/login'

    def test_login_successful(self,client,new_valid_user):
        """Test Login accurate credential"""
        response = client.post(self.url,
                               data = {"email":new_valid_user["email"],
                                       "password":new_valid_user["password"]},
                               format='json')
        assert response.status_code == 200
        assert 'token' in response.data.keys()
        assert 'message' in response.data.keys()

    def test_login_with_incorrect_email(self,client,new_valid_user):
        """Test login with incorrect email"""
        response =client.post(self.url,
                              data ={"email":"email@gmail.com",
                                     "password":new_valid_user["password"]},
                              format='json')
        assert response.status_code == 404
        assert 'errors' in response.data.keys()
        assert response.data['errors'] == 'No account with that email'

    def test_login_with_incorrect_passowrd(self,client,new_valid_user):
        """ test login with incorrect password"""
        response =client.post(self.url,
                              data ={"email":new_valid_user['email'],
                                     "password":"Pass123456"},
                              format='json')
        assert response.status_code == 401
        assert 'error' in response.data.keys()
        assert response.data['error'] == 'Invalid email or password'
