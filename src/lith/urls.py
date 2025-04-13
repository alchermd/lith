from django.urls import path

from .views import index, login, logout, dashboard

app_name = "lith"

urlpatterns = [
    path("", index, name="index"),
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("dashboard/", dashboard, name="dashboard"),
]
