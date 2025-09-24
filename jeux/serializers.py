from rest_framework import serializers
from . import Videogame


class VideogameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videogame
        fields = (
            "id",
            "nom",
            "coop",
            "pvp",
            "joueurs_max_hot_seat",
            "f2p",
            "joueurs_max_online",
        )
