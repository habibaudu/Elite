from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from utils.helpers import BaseModel

class AdminPermission(BaseModel):
    "Admin Permission"

    name = models.CharField(max_length=100)
    allow_make_superadmin = models.BooleanField(default=False)
    allow_delete_user = models.BooleanField(default=False)
    allow_view_users = models.BooleanField(default=False)


class AdminRole(BaseModel):
    "Admin Roles"
    name = models.CharField(max_length =100)
    role_permission = models.ForeignKey(AdminPermission, on_delete=models.CASCADE)


class Admin(AbstractBaseUser, BaseModel):
    "Admin Models"
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True, null=True)
    profile_image = models.URLField(
        default='https://res.cloudinary.com/profile_image.png'
    )
    role = models.ForeignKey(AdminRole, on_delete=models.CASCADE)

    USERNAME_FIELD = "username"

    def __repr__(self):
        return f"<Admin {self.id}>"


