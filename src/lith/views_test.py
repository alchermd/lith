import json

import pytest
from django.test import RequestFactory
from django.urls import reverse

from .models import User
from .views import home, login


def test_hello_world():
    factory = RequestFactory()
    request = factory.get("/")
    response = home(request)
    assert 200 == response.status_code

    json_response = json.loads(response.content)
    assert "hello, world" == json_response["message"]


@pytest.mark.django_db
def test_can_login_using_valid_credentials():
    # Given a user.
    user = User.objects.create(email="foo@example.com")
    user.set_password("test-password")
    user.save()

    # When the user attempts to log in using valid credentials.
    factory = RequestFactory()
    payload = {
        "email": "foo@example.com",
        "password": "test-password",
    }
    request = factory.post(reverse("lith:login"), data=payload)
    response = login(request)

    # Then they get redirected to the dashboard page.
    assert 302 == response.status_code
    # TODO: Replace this with a reverse lookup when the dashboard URL is available.
    assert "/dashboard" == response.url
