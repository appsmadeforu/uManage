from django.contrib.auth.models import User
from django.db import models
from shortuuidfield import ShortUUIDField


class User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.user.username


class Role(models.Model):
    id = ShortUUIDField(primary_key=True)
    role_name = models.TextField()
    description = models.TextField(blank=True)
    role = models.TextField()

    def __str__(self):
        return self.role_name


class Userrole(models.Model):
    id = ShortUUIDField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, blank=True, null=True)  # noqa
