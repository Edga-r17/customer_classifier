from django.urls import path
from .views import classify_client

urlpatterns = [
    path("", classify_client, name="classify_client"),
]
