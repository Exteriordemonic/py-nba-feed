import pytest
from rest_framework.test import APIClient

from users.models import User


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def existing_user(db):
    User.objects.create_user(
        username="test_uesr",
        password="Test_password!@12",
        email="test_email@test.com",
    )


@pytest.mark.django_db
class TestRegiser:
    def test_valid_registration(self, api_client):
        response = api_client.post(
            "/api/auth/register/",
            {
                "username": "test_uesr",
                "password": "Test_password!@12",
                "email": "test_email@test.com",
            },
            format="json",
        )
        assert response.status_code == 201

    def test_invalid_password(self, api_client):
        response = api_client.post(
            "/api/auth/register/",
            {
                "username": "test_uesr",
                "password": "spas",
                "email": "test_email@test.com",
            },
            format="json",
        )

        assert response.status_code == 400

    def test_invalid_email(self, api_client):
        response = api_client.post(
            "/api/auth/register/",
            {
                "username": "test_uesr",
                "password": "Test_password!@12",
                "email": "test_email",
            },
            format="json",
        )

        assert response.status_code == 400

    def test_invalid_username(self, api_client):
        response = api_client.post(
            "/api/auth/register/",
            {
                "username": "",
                "password": "Test_password!@12",
                "email": "test_email@test.com",
            },
            format="json",
        )

        assert response.status_code == 400

    def test_taken_username(self, api_client, existing_user):

        response = api_client.post(
            "/api/auth/register/",
            {
                "username": "test_uesr",
                "password": "Test_password!@12",
                "email": "test_email2@test.com",
            },
            format="json",
        )

        assert response.status_code == 400

    def test_taken_email(self, api_client, existing_user):
        response = api_client.post(
            "/api/auth/register/",
            {
                "username": "test_uesr2",
                "password": "Test_password!@12",
                "email": "test_email@test.com",
            },
            format="json",
        )

        assert response.status_code == 400
