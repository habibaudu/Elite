import pytest

@pytest.mark.django_db

class TestConnection():
    url ='/api/v1/initiate-connection'

    def test_successful_connection(self,client,connection,auth_header):
        response = client.post(self.url,
                               data=connection,
                               format="json",
                               **auth_header)
        assert response.status_code == 201
        assert 'message' in response.data.keys()
        assert  response.data["message"] == "Connection initiated"

    def test_attempt_connecting_to_self(self,client,connection_two,auth_header):
        response = client.post(self.url,
                               data=connection_two,
                               format='json',
                               **auth_header)

        assert response.status_code == 400
        assert response.data['error'] == 'You cannot initiate a connection with yourself'

    def test_connection_already_exist_failure(self,client,connection,auth_header):
        client.post(self.url,
                               data=connection,
                               format="json",
                               **auth_header)
        response = client.post(self.url,
                               data=connection,
                               format='json',
                               **auth_header)
        assert response.status_code == 400
        assert 'error' in response.data.keys()
        assert  response.data["error"] == "Connection already exist"



    def test_failed_connection_attempt(self,client,auth_header):
        response = client.post(self.url,
                               data={"target_user":"invalid_id"},
                               format="json",
                               **auth_header)
        
        assert response.status_code == 404
        assert 'error' in response.data.keys()

    def test_accept_connection_request(self,client,auth_header,new_connection):
        response = client.patch(self.url+"/"+ new_connection['id'],
                                format="json",
                                **auth_header)
        assert response.status_code == 200
        assert response.data['message'] == 'Connection request accepted'

    def test_reject_connection_request(self,client,auth_header,new_connection):
        response = client.delete(self.url+"/"+new_connection["id"],
                                 format="json",
                                 **auth_header)
        assert response.status_code == 200
        assert response.data['message'] == 'Connection request rejected'


    def test_connection_without_auth(self,client,auth_header):
        response = client.patch(self.url,
                                format="json")
        
        assert response.status_code == 403
