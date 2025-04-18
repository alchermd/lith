from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


@login_required
def dashboard(request: HttpRequest) -> HttpResponse:
    context = {
        "email": request.user.email,
    }
    return render(request, "dashboard/dashboard.html", context=context)
