from typing import Callable

from django.contrib import messages
from django.contrib.auth import authenticate, logout as django_logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpRequest, JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.decorators.http import require_http_methods

from .forms.auth import LoginForm
from .models import User


def guest_required(f: Callable) -> Callable:
    """
    Decorator for restricting a view to be only accessible by guests.
    """

    def is_guest(user: User):
        return user.is_anonymous

    decorator = user_passes_test(is_guest, login_url=reverse_lazy("lith:dashboard"))

    if f:
        return decorator(f)

    return decorator


def home(request: HttpRequest) -> HttpResponse:
    return JsonResponse({"message": "hello, world"})


@guest_required
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


@require_http_methods(["POST"])
def logout(request: HttpRequest) -> HttpResponseRedirect:
    django_logout(request)
    return redirect(reverse("lith:login"))


@login_required
def dashboard(request: HttpRequest) -> HttpResponse:
    context = {
        "email": request.user.email,
    }
    return render(request, "lith/dashboard/dashboard.html", context=context)
