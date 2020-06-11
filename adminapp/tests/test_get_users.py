import pytest

@pytest.mark.django_db
class TestGetUsers:
    url1 = '/api/v1/admin/view-users?period=this_month'
    url2 = '/api/v1/admin/view-users?period=this_year'
    url3 = '/api/v1/admin/view-users?period=three_months'

    def test_all_users_this_month(self,client,Admin_auth_header):
        response = client.get(self.url1,
                              format="json",
                              **Admin_auth_header)
        
        assert response.status_code == 200
        assert 'this_month' in response.data.keys()

    def test_all_users_last_three_month(self,client,Admin_auth_header):
        response = client.get(self.url3,
                              format="json",
                              **Admin_auth_header)
        
        assert response.status_code == 200
        assert 'last_three_month' in response.data.keys()

    
    def test_all_users_this_year(self,client,Admin_auth_header):
        response = client.get(self.url2,
                              format="json",
                              **Admin_auth_header)
        
        assert response.status_code == 200
        assert 'this_year' in response.data.keys()

    def test_all_users_without_auth(self,client):
        response = client.get(self.url3,
                              format="json")
        assert response.status_code == 403

    def test_all_users_without_admin_auth(self,client,auth_header):
        response = client.get(self.url3,
                              format="json",
                              **auth_header)
        assert response.status_code == 403
