from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import User, Role
from .auth import hash_password, check_password, create_token


@api_view(["POST"])
def register(request):
    data = request.data

    user_role = Role.objects.get(name="user")

    user = User.objects.create(
        email=data["email"],
        password=hash_password(data["password"]),
        first_name=data.get("first_name", ""),
        last_name=data.get("last_name", ""),
        role=user_role
    )

    return Response({"message": "User created"})


@api_view(["POST"])
def login(request):
    data = request.data

    user = User.objects.filter(email=data["email"]).first()

    if not user:
        return Response({"error": "Invalid credentials"}, status=400)

    if not check_password(data["password"], user.password):
        return Response({"error": "Invalid credentials"}, status=400)

    token = create_token(user.id)

    return Response({"token": token})
