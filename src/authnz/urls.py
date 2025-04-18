from django.urls import path

from .views import login, logout

app_name = "authnz"

urlpatterns = [
    path("login/", login, name="login"),
    path("logout/", logout, name="logout"),
]
