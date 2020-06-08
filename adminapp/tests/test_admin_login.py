import pytest

@pytest.mark.django_db
class TestAdminLogin:
    url ='/api/v1/admin/login'

    def test_admin_login_success(self,client,admin_data):
        response = client.post(self.url,
                               data={"username":admin_data['username'],
                                     "password":admin_data['password']},
                               format='json')
        
        assert response.status_code == 200
        assert response.data['message'] == "Your login was successful"

    def test_admin_login_failure(self,client,admin_data):
        response = client.post(self.url,
                               data={
                                   "username":"wrong username",
                                   "password":admin_data["password"]
                               },
                               fromat='json')

        assert response.status_code == 401
        assert  'error' in response.data.keys()

    def test_admin_login_with_wrong_password(self,client,admin_data):
        response = client.post(self.url,
                               data={
                                   "username":admin_data['username'],
                                   "password":'wrong password'
                               },
                               fromat='json')

        assert response.status_code == 401
        assert  'error' in response.data.keys()
