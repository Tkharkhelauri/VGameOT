from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Game, User, Age, Category
from django.db.models import Q


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ""

    # games = Game.objects.all() #ეს გამოაჩენს ყველა თამაშს, მაგრმ მინდა რომ დაფილტროს
    games = Game.objects.filter(Q(name__icontains=q) | Q(description__icontains=q) | Q(category__name__icontains=q)) #icontains - რეგისტრს არ აქვს მნიშვნელობა
    games = list(set(games))
    categories = Category.objects.all()
    # print(games[0].users.all()) საშუალებას მაძლევს მაგალითად გავიგო რომელიმე თამაში რამდენ user-ს აქვს არჩეული
    heading = "რა ვითამაშოთ???"
    context = {"games": games, "heading": heading, "categories": categories}
    return render(request, 'findgame/home.html', context)


def game_description(request, id):
    game = Game.objects.get(id=id)
    return render(request, 'game_description.html', {'game': game})


def about(request):
    return render(request, 'findgame/about.html')


def contact(request):
    return render(request, 'findgame/contact.html')


def profile(request, pk):
    user = User.objects.get(id=pk) #დაფილტრული იუზერი
    q = request.GET.get('q') if request.GET.get('q') != None else ""

    games = user.games.filter(Q(name__icontains=q) | Q(description__icontains=q) | Q(category__name__icontains=q))  #ეს home-დან დავაკოპირე
    # games = user.games.all() #user-იდან გავდივარ ყველა მის წიგნზე
    games = list(set(games))
    categories = Category.objects.all()

    heading = "ჩემი თამაშები"
    context = {'games': games, 'user': user, "heading": heading, "categories": categories}
    return render(request, 'findgame/profile.html', context)


def lower_navbar(request):
    categories = Category.name.all()  # Fetch all categories from the database
    return render(request, 'lower_navbar.html', {'categories': categories})


def adding(request, id):
    # print(id)
    game = Game.objects.get(id=id)
    user = request.user
    user.games.add(game)
    return redirect('profile', user.id)


def remove(request, id):
    game = Game.objects.get(id=id)

    if request.method == "POST":
        request.user.games.remove(game)
        return redirect('profile', request.user.id)

    return render(request, 'findgame/remove.html', {"game": game})