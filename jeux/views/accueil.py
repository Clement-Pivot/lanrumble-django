from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from ..models import Player, VideogameRating
from .gestionnaire_erreur import gestionnaire_erreur
from .joueur_options import joueur_colors, joueur_background


@login_required(login_url="/")
@gestionnaire_erreur
def accueil(request, error_message=False):
    try:
        player = Player.objects.get(user=request.user.id)
    except Exception:
        request.session["error_message"] += "Utilisateur introuvable.\\n"
        request.session["error_not_seen"] = False
        return redirect("jeux:index")
    else:
        friends = {}
        games = {}
        for friend in player.friends.exclude(user__groups__name="guest").all():
            friends[friend.user.username] = []
            for game in friend.videogames_list.all():
                try:
                    vote = (
                        VideogameRating.objects.filter(joueur_concerne=friend.id)
                        .filter(jeu_concerne=game.id)
                        .get()
                        .rating
                    )
                except Exception:
                    vote = 5
                friends[friend.user.username].append([game.title, vote])

        for game in player.videogames_list.all():
            games[game.title] = {}
            games[game.title]["id"] = game.id
            games[game.title]["pvp"] = game.pvp
            games[game.title]["coop"] = game.coop
            games[game.title]["f2p"] = game.f2p
            games[game.title]["joueurs_online"] = game.max_online_players
            games[game.title]["joueurs_hot_seat"] = game.max_hot_seat_players
            try:
                games[game.title]["my_vote"] = (
                    VideogameRating.objects.filter(player=player.id)
                    .filter(videogame=game.id)
                    .get()
                    .rating
                )
            except Exception:
                games[game.title]["my_vote"] = 5

        if User.objects.get(username=player.user).email == "":
            request.session[
                "error_message"
            ] += "Veuillez remplir votre addresse mail dans Mon Compte.\\n"
            request.session["error_not_seen"] = False

        return render(
            request,
            "jeux/accueil.html",
            {
                "amis": friends,
                "liste_jeux": games,
                "colors": joueur_colors(request.user.id),
                "background_image": joueur_background(request),
            },
        )
