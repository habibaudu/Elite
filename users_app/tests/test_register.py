import pytest

@pytest.mark.django_db 
class TestUserRegister():
    url = '/api/v1/register'
    def test_register_success(self, client, new_user):
        """ Test that a user is created successfully """

        response = client.post(self.url,
                               data=new_user,
                               format='json')

        assert response.status_code == 201
        assert 'message' in response.data.keys()
        assert response.data['message'] == 'Your registerition with Invent is successfully'

    def test_register_with_invalid_password(self, client, new_user):
        """ Test register with invalid password"""
        new_user["password"] = "pass123"
        response = client.post(self.url,
                               data=new_user,
                               format='json')
        
        assert response.status_code == 400
        assert 'errors' in response.data.keys()

    def test_register_with_invalid_name(self, client, new_user):
        """ Test register with invalid name"""
        new_user["first_name"] = "re@"
        response = client.post(self.url,
                               data= new_user,
                               format='json')
        
        assert response.status_code == 400
        assert 'errors' in response.data.keys()

    def test_register_with_invalid_email(self, client, new_user):
        """ Test register with invalid email"""
        new_user["email"] = "3@utiytyauis"
        response = client.post(self.url,
                               data=new_user,
                               format='json')
        
        assert response.status_code == 400
        assert 'errors' in response.data.keys()