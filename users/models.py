from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError("Phone is required")

        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(phone, password, **extra_fields)


class User(AbstractUser):
    username = None          # remove username completely
    phone = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=100)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    objects = UserManager()  # 🔥 THIS LINE FIXES EVERYTHING

    def __str__(self):
        return self.name
