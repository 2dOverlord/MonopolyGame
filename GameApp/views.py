from django.shortcuts import render


def render_games_page(request):
    return render(request, 'games/games.html')

