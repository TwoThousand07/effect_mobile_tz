from rest_framework.response import Response
from rest_framework.decorators import api_view

from .services import has_permission
from .models import Permission

@api_view(["POST"])
def update_permission(request):
    if not request.user:
        return Response({"error": "Unauthoraized"}, status=401)
    
    if request.user.role.name != "admin":
        return Response(status=403)
    
    data = request.data
    
    perm = Permission.objects.get(id=data["id"])
    
    perm.can_read = data.get("can_read", perm.can_read)
    perm.can_create = data.get("can_create", perm.can_create)
    perm.can_update = data.get("can_update", perm.can_update)
    perm.can_delete = data.get("can_delete", perm.can_delete)
    
    perm.save()
    
    return Response({"message": "updated"})