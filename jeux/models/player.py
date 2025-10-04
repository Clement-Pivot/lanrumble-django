from django.db import models
from django.contrib.auth.models import User
from . import Videogame


def user_directory_path(instance, filename):
    return "user_{0}/{1}".format(instance.utilisateur_id, filename)


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField("self", blank=True)
    videogames_list = models.ManyToManyField(Videogame, blank=True)
    color_body_background = models.CharField(max_length=7, default="#222222")
    color_body_text = models.CharField(max_length=7, default="#ffffff")
    color_nav_background = models.CharField(max_length=7, default="#111111")
    color_nav_link_active = models.CharField(max_length=7, default="#ff0000")
    color_nav_link_hover = models.CharField(max_length=7, default="#ffffff")
    color_nav_link = models.CharField(max_length=7, default="#990000")
    color_nav_text = models.CharField(max_length=7, default="#ffffff")
    background_file = models.FileField(upload_to=user_directory_path, blank=True)

    objects = models.Manager()
    delete_files = models.Manager()

    def __str__(self):
        return self.user.username

    def user_directory_path(*args):
        return user_directory_path(*args)
