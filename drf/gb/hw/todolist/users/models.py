from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, \
    AbstractUser
from rest_framework.authtoken.models import Token


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.username = extra_fields.get('username') if extra_fields.get('username') else email
        user.set_password(password)
        user.save(using=self._db)
        Token.objects.create(user=user)

        return user

    def create_anonymous_user(self):
        """Creates and saves a new superuser"""
        user = self.model()
        user.is_anonymous = True
        user.save(using=self._db)
        Token.objects.create(user=user)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Creates and saves a new superuser"""
        user = self.create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractUser):
    """Custom user model with unique username and email"""
    username = models.CharField(max_length=64, unique=True)
    email = models.EmailField(max_length=64, unique=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    is_anonymous = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f'username: {self.username} (first_name: {self.first_name} last_name:{self.last_name})'

    def update_token(self):
        Token.objects.get(user=self).delete()
        Token.objects.create(user=self)
        print(f'updated token for {self}')
