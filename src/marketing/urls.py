from django.urls import path

from .views import index

app_name = "marketing"

urlpatterns = [
    path("", index, name="index"),
]
