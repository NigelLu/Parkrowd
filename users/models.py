"""customized user model
"""
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    """customized user class
    """
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name="Date Joined", default=timezone.now)

    description = models.TextField()

    # is_superuser : User can create, edit, and delete ANY object (models)
    is_superuser = models.BooleanField(default=False)
    # is_staff : User can login to site
    is_staff = models.BooleanField(default=False)
    # is_admin : User is treated as non-superuser staff member.
    # Admins can be customized to have certain permissions.
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return f"Email: {self.email}\n" f"Username: {self.username}\n"

    @staticmethod
    def has_perm(perm, obj=None, **kwargs):
        """TODO: why overriding the original implementation here"""
        return True

    @staticmethod
    def has_module_perms(app_label, **kwargs):
        """TODO: why overriding the original implementation here"""
        return True
