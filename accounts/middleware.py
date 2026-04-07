from django.utils.deprecation import MiddlewareMixin

from .models import User
from .auth import decode_token


class AuthMiddleware(MiddlewareMixin):
    def process_token(self, request):
        auth_header = request.headers.get("Authorization")
        
        if not auth_header:
            request.user = None
            return 
        
        try:
            token = auth_header.splite(" ")[1]
            payload = decode_token(token)
            
            if not payload:
                request.user = None
                return
            
            user = User.objects.get(id=payload["user_id"])
            
            if not user.is_active:
                request.user = None
                return
        except:
            request.user = None