from rest_framework.response import Response
from rest_framework.decorators import api_view

from permissions.services import has_permission
from permissions.decorators import permission_required


@api_view(["GET"])
@permission_required("products", "read")
def products(request):
    # if not request.user:
    #     return Response({"error": "Unauthoraized"}, status=401)

    # if not has_permission(request.user, "products", "read"):
    #     return Response({"error": "Forbidden"}, status=403)

    return Response(["item1", "item2"])


@api_view(["POST"])
def create_products(request):
    if not request.user:
        return Response({"error": "Unauthoraized"}, status=401)

    if not has_permission(request.user, "products", "read"):
        return Response({"error": "Forbidden"}, status=403)
    
    return Response({"message": "created"})
