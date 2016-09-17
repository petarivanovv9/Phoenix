from django.db import models
from website.models import (Profile)


class Chat(models.Model):
    name = models.CharField(max_length=20, blank=True, default="", null=True)
    users = models.ManyToManyField(Profile)

    def __str__(self):
        return self.name


class Message(models.Model):
    content = models.CharField(max_length=255, blank=True, default="", null=True)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.chat.name, self.user.username)
