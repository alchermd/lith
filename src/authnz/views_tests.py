import pytest
from django.test import Client
from django.urls import reverse

from .models import User


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
    response = client.post(reverse("authnz:login"), data=payload)

    # Then the user is redirected to the dashboard page
    assert 302 == response.status_code
    assert reverse("dashboard:dashboard") in response.url

    # ... and the user's session is authenticated
    assert response.wsgi_request.user.is_authenticated


@pytest.mark.django_db
def test_login_with_invalid_credentials_shows_an_error_message(client: Client):
    # When an invalid set of credentials are used to log in.
    payload = {
        "email": "unauthenticated@example.com",
        "password": "test-password",
    }
    response = client.post(reverse("authnz:login"), data=payload)

    # Then the response returns an unauthorized status code
    assert 401 == response.status_code

    # ... and a helpful error message.
    assert "Invalid credentials" in response.content.decode("utf-8")


def test_login_page_can_be_accessed_by_guests(client: Client):
    # When a guest accesses the login page
    response = client.get(reverse("authnz:login"))

    # Then the guest gets a successful response
    assert 200 == response.status_code


@pytest.mark.django_db
def test_user_can_logout_to_terminate_session(client: Client):
    # Given an existing user that is logged in
    user = User.objects.create(email="foo@example.com")
    user.set_password("test-password")
    user.save()
    client.login(username="foo@example.com", password="test-password")

    # When the user sends a request to logout
    response = client.post(reverse("authnz:logout"))

    # Then the user's session ends
    assert response.wsgi_request.user.is_anonymous

    # ... and is redirected to the login page
    assert 302 == response.status_code
    assert reverse("authnz:login") in response.url


@pytest.mark.django_db
def test_user_gets_a_message_when_they_log_out(client: Client):
    # Given an existing user that is logged in
    user = User.objects.create(email="foo@example.com")
    user.set_password("test-password")
    user.save()
    client.login(username="foo@example.com", password="test-password")

    # When the user sends a request to logout
    response = client.post(reverse("authnz:logout"), follow=True)

    # Then the response comes with an informational message
    assert "You have been logged out" in response.content.decode("utf-8")


def test_logout_is_not_accessible_via_GET(client: Client):
    # When a GET request is issued to the logout view
    response = client.get(reverse("authnz:logout"))

    # Then a method not allowed response is returned
    assert 405 == response.status_code
