from rest_framework.views import APIView
from rest_framework.response import Response
from jeux.models import Videogame
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404


class VideogameView(APIView):
    def get(self, request, id):
        try:
            game = Videogame.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise Http404
        return Response(
            {
                "name": game.title,
                "id": game.pk,
                "coop": game.coop,
                "pvp": game.pvp,
                "max_hot_seat_players": game.max_hot_seat_players,
                "max_online_players": game.max_online_players,
                "f2p": game.f2p,
                "steam_id": game.steam_id,
                "status": game.status,
            }
        )
