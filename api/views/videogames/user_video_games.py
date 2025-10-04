from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from jeux.models import Player


class UserVideogamesView(APIView):
    permission_classes = (IsAuthenticated,)

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

        try:
            current_user = Player.objects.prefetch_related("user").get(
                pk=request.user.id
            )
            friends = current_user.friends.exclude(user__groups__name="guest")

            if str(request.user.id) != user_id and not user_id in [
                str(x.id) for x in friends
            ]:
                raise HttpResponse("Unauthorized", status=401)

            player = Player.objects.get(pk=user_id)
            all_games = player.videogames_list.all()
        except ObjectDoesNotExist:
            raise Http404
        return Response([extract_data(x) for x in all_games])
