from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework import status
import pytest


@pytest.fixture
def create_collection(api_client):
    def do_create_collection(collection):
        return api_client.post('/store/collections/', collection)
    return do_create_collection


@pytest.mark.django_db
class TestCreateCollection:
    def test_if_user_is_anonymous_returns_401(self, create_collection):
        # AAA (Arrange, Act, Assert
        response = create_collection({'title': 'a'})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_admin_returns_403(self, api_client, create_collection):
        api_client.force_authenticate(user={})
        response = create_collection({'title': 'a'})
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_returns_400(self, api_client, create_collection):

        api_client.force_authenticate(user=User(is_staff=True))
        response = create_collection({'title': ''})
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['title'] is not None

    def test_if_data_is_valid_returns_201(self, api_client, create_collection):
            api_client.force_authenticate(user=User(is_staff=True))
            response = create_collection({'title': 'a'})
            assert response.status_code == status.HTTP_201_CREATED
            assert response.data['id'] > 0




