from django.contrib.auth import authenticate
from django.http import HttpRequest, JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect


def home(request: HttpRequest) -> HttpResponse:
    return JsonResponse({"message": "hello, world"})


def login(request: HttpRequest) -> HttpResponseRedirect | None:
    email = request.POST.get("email")
    password = request.POST.get("password")

    user = authenticate(username=email, password=password)

    if user is not None:
        return redirect("/dashboard")
