from django.db import models
from rest_framework import serializers


class Videogame(models.Model):
    title = models.CharField(max_length=100, unique=True)
    coop = models.BooleanField(default=False)
    pvp = models.BooleanField(default=False)
    max_hot_seat_players = models.SmallIntegerField(default=1)
    max_online_players = models.SmallIntegerField(default=0)
    f2p = models.BooleanField(default=False)
    steam_id = models.BigIntegerField(default=None, blank=True, null=True)
    status = models.CharField(max_length=100, default="live")

    def __str__(self):
        return self.title


class VideogameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videogame
        fields = "__all__"
        # exclude = ["id"]

    def save(self):
        self.instance.title = self.validated_data.get("title", self.instance.title)
        self.instance.coop = self.validated_data.get("coop", self.instance.coop)
        self.instance.pvp = self.validated_data.get("pvp", self.instance.pvp)
        self.instance.max_hot_seat_players = self.validated_data.get(
            "max_hot_seat_players", self.instance.max_hot_seat_players
        )
        self.instance.max_online_players = self.validated_data.get(
            "max_online_players", self.instance.max_online_players
        )
        self.instance.f2p = self.validated_data.get("f2p", self.instance.f2p)
        self.instance.steam_id = self.validated_data.get(
            "steam_id", self.instance.steam_id
        )
        self.instance.status = self.validated_data.get("status", self.instance.status)
        return self.instance.save()
