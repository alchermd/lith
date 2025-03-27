import json

from django.test import RequestFactory

from .views import home


def test_hello_world():
    factory = RequestFactory()
    request = factory.get("/")
    response = home(request)
    assert 200 == response.status_code

    json_response = json.loads(response.content)
    assert "hello, world" == json_response["message"]
