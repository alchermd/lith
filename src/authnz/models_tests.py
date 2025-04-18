import pytest
from django.db import IntegrityError

from .models import User


@pytest.mark.django_db
def test_email_is_case_insensitive_unique():
    User.objects.create(email="foo@example.com")

    with pytest.raises(IntegrityError):
        User.objects.create(email="Foo@example.com")
