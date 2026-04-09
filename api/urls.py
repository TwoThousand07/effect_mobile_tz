from django.urls import path, include

from .views import products, create_products

urlpatterns = [
    path("auth/", include("accounts.urls")),
    path("permissions/", include("permissions.urls")),
    path("products/", products),
    path("products/", create_products)
]
