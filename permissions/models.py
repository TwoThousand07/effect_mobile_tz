from django.db import models

from accounts.models import Role


class Permission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    
    resource = models.CharField(max_length=50)
    
    can_read = models.BooleanField(default=False)
    can_create = models.BooleanField(default=False)
    can_update = models.BooleanField(default=False)
    can_delete = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.role} - {self.resource}"
    
