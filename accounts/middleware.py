from django.utils.deprecation import MiddlewareMixin

from .models import User
from .auth import decode_token


class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.user = None
        auth_header = request.headers.get("Authorization")
        
        if not auth_header:
            return 
        
        try:
            parts = auth_header.split(" ")
            if len(parts) != 2 or parts[0] != "Bearer":
                return
            
            token = parts[1]
            payload = decode_token(token)
            
            if not payload:
                return
            
            user = User.objects.get(id=payload["user_id"])
            
            if not user.is_active:
                request.user = None
                return
            
            request.user = user
        except:
            request.user = None