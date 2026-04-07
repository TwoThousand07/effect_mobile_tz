from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email