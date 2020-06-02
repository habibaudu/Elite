import json
import pytest

@pytest.mark.django_db

class TestUserProgfile():
    url ='/api/v1/user-profile'

    def test_getuser_profile_success(self,client,auth_header):
        """ test user profile success """

        response = client.get(self.url,
                              format="json",
                              **auth_header)

        assert response.status_code == 200
        assert "message" in response.data.keys()
        assert response.data["message"] == 'Successfully retrived your user information'

    def test_getuser_profile_failed(self,client):
        response = client.get(self.url,
                              format="json")
        
        assert response.status_code == 403
        assert "error" in response.data.keys()