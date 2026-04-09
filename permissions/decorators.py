from functools import wraps

from .services import has_permission

from rest_framework.response import Response


def permission_required(resource, action):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            user = request.user

            if not user or not hasattr(user, "role"):
                return Response({"error": "Unauthorized"}, status=401)

            if not has_permission(user, resource, action):
                return Response({"error": "Forbidden"}, status=403)

            return view_func(request, *args, **kwargs)

        return wrapper
    return decorator
