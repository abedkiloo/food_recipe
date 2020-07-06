from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """ creates and saves a new user"""
        if not email:
            raise ValueError("users Must a valid email")
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_super_user(self, email, password):
        """creates and save new user user"""
        user = self.create_user(email=email, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self.db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """custom user model that support email instead of user name"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
