from django.db import models
from . import Videogame
from . import Player


class VideogameRating(models.Model):
    rating = models.SmallIntegerField(default=5)
    videogame = models.ForeignKey(
        Videogame,
        blank=False,
        on_delete=models.CASCADE,
        db_column="jeu_concerne",
    )
    player = models.ForeignKey(
        Player,
        blank=False,
        on_delete=models.CASCADE,
        db_column="joueur_concerne",
    )

    def __str__(self):
        return (
            self.player.user.username
            + " - "
            + self.videogame.title
            + " = "
            + str(self.rating)
        )
