from rest_framework.views import APIView
from rest_framework.response import Response
from jeux.models import Videogame


class VideogamesView(APIView):
    def get(self, request):
        all_games = Videogame.objects.all()
        return Response(
            list(
                map(
                    lambda jeu: {
                        "name": jeu.title,
                        "id": jeu.pk,
                        "coop": jeu.coop,
                        "pvp": jeu.pvp,
                        "max_hot_seat_players": jeu.max_hot_seat_players,
                        "max_online_players": jeu.max_online_players,
                        "f2p": jeu.f2p,
                        "steam_id": jeu.steam_id,
                        "status": jeu.status,
                    },
                    all_games,
                )
            )
        )
