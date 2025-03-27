from django.http import HttpRequest, JsonResponse, HttpResponse


def home(request: HttpRequest) -> HttpResponse:
    return JsonResponse({"message": "hello, world"})
