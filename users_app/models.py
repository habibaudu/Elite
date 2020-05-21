from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

from users_app.utils.id_genrator import generate_id, LENGTH_OF_ID


class UserManager(BaseUserManager):
    def create_user(self, **kwargs):
        """
        Creates and saves a User with email, password credentials.
        """
        email = kwargs.get("email")
        password = kwargs.get("password")
        first_name = kwargs.get("first_name")
        last_name = kwargs.get("last_name")
        user = self.model(email=self.normalize_email(email).lower(),
            first_name=first_name, last_name=last_name,
        )
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
        User model
    """

    id = models.CharField(
        max_length=LENGTH_OF_ID, primary_key=True, default=generate_id,
        editable=False
    )
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, unique=True)
    password = models.CharField(max_length=100, null=False)
    profile_image = models.URLField(
        default='https://res.cloudinary.com/some_profile_image.png'
    )
    gender = models.CharField(max_length=50, null=True)
    birthday = models.DateField(auto_now=False, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = "email"

    objects = UserManager()

    def __str__(self):
        return self.email

