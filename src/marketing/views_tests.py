import pytest
from django.test import Client
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_can_access_index_page(client: Client):
    # When a guest accesses the dashboard page
    response = client.get(reverse("marketing:index"))

    # Then the user is redirected to the login page
    assert 200 == response.status_code
    assertTemplateUsed(response, "marketing/landing-page.html")
