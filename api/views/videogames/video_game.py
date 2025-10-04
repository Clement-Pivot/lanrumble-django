from rest_framework.views import APIView
from rest_framework.response import Response
from jeux.models import Videogame, VideogameSerializer
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
from django.http import Http404


class VideogameView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, _, id):
        try:
            game = Videogame.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise Http404
        return Response(VideogameSerializer(game).data)

    def put(self, request, id):
        try:
            game = Videogame.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise Http404
        data = VideogameSerializer(game, data=request.data)
        if data.is_valid(raise_exception=True):
            data.save()
        return Response(data.data)
