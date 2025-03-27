from django.http import HttpRequest, JsonResponse, HttpResponse


def home(request: HttpRequest) -> HttpResponse: # This should trigger a PEP8 violation for being too long of a line.
    return JsonResponse({"message": "hello, world"})
