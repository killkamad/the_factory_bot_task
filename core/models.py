from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    telegram_id = models.IntegerField(unique=True, null=True)
    telegram_token = models.CharField(max_length=256, null=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=64)


class Messages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message_body = models.TextField(max_length=1000)
    date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user} | {self.date_time}'
