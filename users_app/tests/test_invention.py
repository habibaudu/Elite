import pytest

@pytest.mark.django_db
class TestInvention:
    url ="/api/v1/add-invention"

    def test_invention(self,client,auth_header,invention_data):
        response = client.post(self.url,
                               data=invention_data,
                               format="json",
                               **auth_header
                                )
        assert 'message' in response.data.keys()
        assert response.status_code == 201

    def test_invention_fail(self,client,auth_header,invention_data):
        response = client.post(self.url,
                               data={
                                   'invent_media':"invalid url",
                                   'title':invention_data['title'],
                                   'about_invention':invention_data["about_invention"],
                                   'location':invention_data['location']
                               },
                               format="json",
                               **auth_header
                                )
        assert 'errors' in response.data.keys()
        assert response.status_code == 400

    def test_invention_fail_invalid_title(self,client,auth_header,invention_data):
        response = client.post(self.url,
                               data={
                                   'invent_media':invention_data['invent_media'],
                                   'title':'id',
                                   'about_invention':invention_data["about_invention"],
                                   'location':invention_data['location']
                               },
                               format="json",
                               **auth_header
                                )
        assert 'errors' in response.data.keys()
        assert response.status_code == 400

    def test_invention_fail_invalid_about_invention(self,client,auth_header,invention_data):
        response = client.post(self.url,
                               data={
                                   'invent_media':invention_data['invent_media'],
                                   'title':invention_data['title'],
                                   'about_invention':'very short',
                                   'location':invention_data['location']
                               },
                               format="json",
                               **auth_header
                                )
        
        assert 'errors' in response.data.keys()
        assert response.status_code == 400

    def test_invention_without_authorization(self,client,invention_data):
        response = client.post(self.url,
                               data=invention_data,
                               format="json"
                                )
        
        assert 'error' in response.data.keys()
        assert response.status_code == 403
