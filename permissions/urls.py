from django.urls import path

from .views import update_permission

urlpatterns = [
    path("update/", update_permission)
]
