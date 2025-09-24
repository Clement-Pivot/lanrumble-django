from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from jeux.models import Player, Videogame


class UserVideogamesView(APIView):
    permission_classes = (IsAuthenticated,)
    # TODO : check if user ID == request ID

    def get(self, request, user_id):
        def extract_data(jeu):
            return {
                "name": jeu.title,
                "id": jeu.pk,
                "coop": jeu.coop,
                "pvp": jeu.pvp,
                "max_hot_seat_players": jeu.max_hot_seat_players,
                "max_online_players": jeu.max_online_players,
                "f2p": jeu.f2p,
                "steam_id": jeu.steam_id,
                "status": jeu.status,
            }

        player = Player.objects.get(pk=user_id)
        try:
            all_games = player.videogames_list.all()
        except ObjectDoesNotExist:
            raise Http404
        return Response(list(map(extract_data, all_games)))
