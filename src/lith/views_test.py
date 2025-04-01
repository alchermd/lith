import json

import pytest
from django.test import RequestFactory, Client
from django.urls import reverse

from .models import User
from .views import home


def test_hello_world():
    factory = RequestFactory()
    request = factory.get("/")
    response = home(request)
    assert 200 == response.status_code

    json_response = json.loads(response.content)
    assert "hello, world" == json_response["message"]


@pytest.mark.django_db
def test_can_login_using_valid_credentials(client: Client):
    # Given a user.
    user = User.objects.create(email="foo@example.com")
    user.set_password("test-password")
    user.save()

    # When the user attempts to log in using valid credentials.
    payload = {
        "email": "foo@example.com",
        "password": "test-password",
    }
    response = client.post(reverse("lith:login"), data=payload)

    # Then they get redirected to the dashboard page.
    assert 302 == response.status_code
    # TODO: Replace this with a reverse lookup when the dashboard URL is available.
    assert "/dashboard" == response.url


@pytest.mark.django_db
def test_login_with_invalid_credentials_shows_an_error_message(client: Client):
    # When an invalid set of credentials are used to log in.
    payload = {
        "email": "unauthenticated@example.com",
        "password": "test-password",
    }
    response = client.post(reverse("lith:login"), data=payload)

    # Then the response returns an unauthorized status code
    assert 401 == response.status_code

    # ... and a helpful error message.
    assert "Invalid credentials" in response.content.decode("utf-8")


@pytest.mark.django_db
def test_authenticated_users_can_access_the_dashboard(client: Client):
    # Given an existing user
    user = User.objects.create(email="foo@example.com")
    user.set_password("test-password")
    user.save()

    # When that user is logged in and accesses the dashboard page
    client.login(username="foo@example.com", password="test-password")
    response = client.get(reverse("lith:dashboard"))

    # Then the user gets a successful response
    assert 200 == response.status_code


@pytest.mark.django_db
def test_guests_get_redirected_to_login_when_accessing_the_dashboard(client: Client):
    # When a guest accesses the dashboard page
    response = client.get(reverse("lith:dashboard"))

    # Then the user is redirected to the login page
    assert 302 == response.status_code
    assert reverse("lith:login") in response.url


def test_login_page_can_be_accessed_by_guests(client: Client):
    # When a guest accesses the login page
    response = client.get(reverse("lith:login"))

    # Then the guest gets a successful response
    assert 200 == response.status_code


@pytest.mark.django_db
def test_authenticated_users_get_redirected_to_dashboard_when_accessing_the_login_page(
    client: Client,
):
    # Given an existing user
    user = User.objects.create(email="foo@example.com")
    user.set_password("test-password")
    user.save()

    # When that user accesses the login page
    client.login(username="foo@example.com", password="test-password")
    response = client.get(reverse("lith:login"))

    # Then the user is redirected to the dashboard
    assert 302 == response.status_code
    assert reverse("lith:dashboard") in response.url


@pytest.mark.django_db
def test_user_can_logout_to_terminate_session(client: Client):
    # Given an existing user that is logged in
    user = User.objects.create(email="foo@example.com")
    user.set_password("test-password")
    user.save()
    client.login(username="foo@example.com", password="test-password")

    # When the user sends a request to logout
    response = client.post(reverse("lith:logout"))

    # Then the user's session ends
    assert response.wsgi_request.user.is_anonymous

    # ... and is redirected to the login page
    assert 302 == response.status_code
    assert reverse("lith:login") in response.url


def test_logout_is_not_accessible_via_GET(client: Client):
    # When a GET request is issued to the logout view
    response = client.get(reverse("lith:logout"))

    # Then a method not allowed response is returned
    assert 405 == response.status_code
