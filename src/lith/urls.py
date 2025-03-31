from django.urls import path

from .views import login, dashboard

app_name = "lith"

urlpatterns = [
    path("login/", login, name="login"),
    path("dashboard/", dashboard, name="dashboard"),
]
