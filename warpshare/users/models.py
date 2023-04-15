from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        email=self.normalize_email(email)
        user=self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(username, email, password, **extra_fields)


# Create your models here.
class User(AbstractUser):
    id=models.BigAutoField(primary_key=True, null=False, auto_created=True)
    email=models.EmailField(null=False, blank=False, unique=True)
    username=models.CharField(max_length=20, null=False)
    password=models.CharField(max_length=250, null=False, blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

    objects=CustomUserManager()
    USERNAME_FIELD: str = 'email'
    REQUIRED_FIELDS: list = ['username']

    def __str__(self) -> str:
        return f'User id: {self.id}, username: {self.username}, password: {self.password}'

