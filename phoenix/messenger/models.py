from django.db import models
from django.contrib.auth.models import User

from datetime import datetime


class UserProfile(models.Model):
    user = models.ForeignKey(User)


class Chat(models.Model):
    name = models.CharField(max_length=20, blank=True, default="", null=True)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class Message(models.Model):
    content = models.CharField(max_length=255, blank=True, default="", null=True)
    chat = models.ForeignKey(Chat)
    user = models.ForeignKey(User)

    def __str__(self):
        return "{} - {}".format(chat.name, user.username)
