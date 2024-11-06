from django.contrib import admin
from django.urls import include, path

# Inlcude basically allows many different link functions without listing them
urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]