from django.db import models
from django.conf import settings

# Create your models here.


class User(models.Model):
    user = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="users"
    )
