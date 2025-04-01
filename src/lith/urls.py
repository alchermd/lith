from django.urls import path

from .views import login, logout, dashboard

app_name = "lith"

urlpatterns = [
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
    path("dashboard/", dashboard, name="dashboard"),
]
