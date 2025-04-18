import pytest
from django.test import Client
from django.urls import reverse

from authnz.models import User


@pytest.mark.django_db
def test_authenticated_users_can_access_the_dashboard(client: Client):
    # Given an existing user
    user = User.objects.create(email="foo@example.com")
    user.set_password("test-password")
    user.save()

    # When that user is logged in and accesses the dashboard page
    client.login(username="foo@example.com", password="test-password")
    response = client.get(reverse("dashboard:dashboard"))

    # Then the user gets a successful response
    assert 200 == response.status_code


@pytest.mark.django_db
def test_guests_get_redirected_to_login_when_accessing_the_dashboard(client: Client):
    # When a guest accesses the dashboard page
    response = client.get(reverse("dashboard:dashboard"))

    # Then the user is redirected to the login page
    assert 302 == response.status_code
    assert reverse("authnz:login") in response.url


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
    response = client.get(reverse("authnz:login"))

    # Then the user is redirected to the dashboard
    assert 302 == response.status_code
    assert reverse("dashboard:dashboard") in response.url
