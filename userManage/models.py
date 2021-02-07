from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Role(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    role_name = models.TextField()
    description = models.TextField(blank=True)
    role = models.TextField()

    def __str__(self):
        return self.role_name


class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, blank=True, null=True)  # noqa
