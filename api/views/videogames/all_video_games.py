from rest_framework.views import APIView
from rest_framework.response import Response
from jeux.models import Videogame, VideogameSerializer


class VideogamesView(APIView):
    def get(self, _):
        all_games = Videogame.objects.all()
        return Response([VideogameSerializer(jeu).data for jeu in all_games])

    def post(self, request):
        data = VideogameSerializer(data=request.data)
        if data.is_valid(raise_exception=True):
            data.save()
