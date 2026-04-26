import pytest


from users.serializers import UserSerializer


@pytest.mark.django_db
def test_valid_password():
    data = {
        "username": "test_uesr",
        "password": "Test_password!@12",
        "email": "test_email@test.com",
    }

    serializer = UserSerializer(data=data)

    assert serializer.is_valid()


@pytest.mark.django_db
def test_short_password():
    data = {
        "username": "test_uesr",
        "password": "Test_",
        "email": "test_email@test.com",
    }

    serializer = UserSerializer(data=data)

    assert not serializer.is_valid()
