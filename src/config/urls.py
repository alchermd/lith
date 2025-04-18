from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("authnz.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("", include("marketing.urls")),
]
