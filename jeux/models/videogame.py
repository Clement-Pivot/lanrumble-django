from django.db import models


class Videogame(models.Model):
    title = models.CharField(max_length=100, unique=True)
    coop = models.BooleanField(default=False)
    pvp = models.BooleanField(default=False)
    max_hot_seat_players = models.SmallIntegerField(default=1)
    max_online_players = models.SmallIntegerField(default=0)
    f2p = models.BooleanField(default=False)
    steam_id = models.BigIntegerField(default=1)
    status = models.CharField(max_length=100, default="live")

    def __str__(self):
        return self.title
