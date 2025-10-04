#!/usr/bin/python3
from django.core.management.base import BaseCommand, CommandError

from jeux.models import Videogame, Player, VideogameRating
from django.db import transaction


class Command(BaseCommand):
    help = "Usage : call command to run custom migrations"

    @transaction.atomic
    def handle(self, *args, **options):
        jeux_presents = Videogame.objects.all()
        for jeu in jeux_presents:
            jeu.steam_id = None if jeu.steam_id == 1 else jeu.steam_id
            jeu.save()
        self.stdout.write(self.style.SUCCESS("JOB DONE !"))
