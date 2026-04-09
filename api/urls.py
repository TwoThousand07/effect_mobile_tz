from django.urls import path, include

urlpatterns = [
    path("auth/", include("accounts.urls")),
    path("permissions/", include("permissions.urls"))
]
