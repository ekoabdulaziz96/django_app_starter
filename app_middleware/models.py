from django.db import models
from django.contrib.auth.models import AbstractUser
from .models_role import Role as RoleModel


# Create your models here.
class User(AbstractUser):
    role = models.ForeignKey(RoleModel, on_delete=models.CASCADE, null=True)
    other = models.CharField(max_length=200,default='-',null=True)
