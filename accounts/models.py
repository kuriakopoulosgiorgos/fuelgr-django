from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth import get_user_model


from accounts.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=45, unique=True, db_index=True, primary_key=True)
    email = models.EmailField('email address', unique=True)

    objects=UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "users"
        verbose_name = 'user'
        verbose_name_plural = 'users'