from django.db import models


class User(models.Model):
    username = models.CharField(max_length=256)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
