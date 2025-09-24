from django.db import models
from django.contrib.auth.models import User
from datetime import time
from . import Player


class Boardgame(models.Model):
    title = models.CharField(max_length=100, unique=True)
    game_time = models.TimeField(default=time(1, 1))
    max_players = models.SmallIntegerField(default=1)
    min_players = models.SmallIntegerField(default=1)
    difficulty = models.SmallIntegerField(default=1)
    owned_by = models.ManyToManyField(Player, blank=True)

    def __str__(self):
        return self.title
