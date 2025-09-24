from django.db import models
from django.contrib.auth.models import User


class TokenResetPassword(models.Model):
    utilisateur_id = models.ForeignKey(User, blank=False, on_delete=models.CASCADE)
    token = models.CharField(max_length=100, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            self.utilisateur_id.username
            + " @ "
            + self.created.strftime("%d/%m/%Y %H:%M:%S")
            + " UTC"
        )
