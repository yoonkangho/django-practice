# built-in imports

# third party imports
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

# application imports
from .base import BaseModel, BaseManager


class UserManager(BaseManager, UserManager):
    pass


class User(BaseModel, AbstractBaseUser, PermissionsMixin):

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        max_length=150, unique=True, validators=[username_validator]
    )

    email = models.EmailField(unique=True)

    is_staff = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    objects = UserManager()

    class Meta:
        abstract = False
