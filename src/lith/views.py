from django.contrib import messages
from django.contrib.auth import authenticate
from django.http import HttpRequest, JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from .forms.auth import LoginForm


def home(request: HttpRequest) -> HttpResponse:
    return JsonResponse({"message": "hello, world"})


def login(request: HttpRequest) -> HttpResponseRedirect | HttpRequest:
    status = 200
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            user = authenticate(username=email, password=password)

            if user is not None:
                return redirect("/dashboard")

            messages.error(request, "Invalid credentials")
            status = 401
    else:
        form = LoginForm()

    context = {
        "form": form,
    }

    return render(request, "lith/auth/login.html", context=context, status=status)
