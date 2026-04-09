from .models import Permission

def has_permission(user, resource, action):
    if not user:
        return False
    
    if not user.role:
        return False
    
    permission = Permission.objects.filter(role=user.role, resource=resource).first()
    
    if not permission:
        return False
    
    return getattr(permission, f"can_{action}", False)