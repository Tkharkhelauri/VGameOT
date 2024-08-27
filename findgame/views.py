from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Game, User, Age, Category, Comment
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import AppUserCreationForm, UserChangeForm, GameForm, UserForm, UserUpdateForm
from .seeder import seeder_func
from django.contrib import messages


def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    seeder_func()
    # games = Game.objects.all() #ეს გამოაჩენს ყველა თამაშს, მაგრმ მინდა რომ დაფილტროს
    games = Game.objects.filter(Q(name__icontains=q) | Q(description__icontains=q) | Q(category__name__icontains=q)) #icontains - რეგისტრს არ აქვს მნიშვნელობა
    games = list(dict.fromkeys(games))
    categories = Category.objects.all()
    # print(games[0].users.all()) საშუალებას მაძლევს მაგალითად გავიგო რომელიმე თამაში რამდენ user-ს აქვს არჩეული
    heading = "რა ვითამაშოთ???"
    context = {"games": games, "heading": heading, "categories": categories}
    return render(request, 'findgame/home.html', context)


def game_description(request, id):
    game = Game.objects.get(id=id)

    game_comments = game.comment_set.all().order_by('-created')
    if request.method == 'POST':
        comment = Comment.objects.create(
            user=request.user,
            game=game,
            body=request.POST.get('body')
        )
    context = {
        'game': game,
        'comments': game_comments
    }
    return render(request, 'findgame/game_description.html', context)


def delete_comment(request, id):
    comment = Comment.objects.get(id=id)
    game = comment.game
    if request.method == 'POST':
        comment.delete()
        return redirect('reading', game.id)
    return render(request, 'findgame/del-comment.html', {'obj': comment})

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


@login_required(login_url='login')
def remove(request, id):
    game = Game.objects.get(id=id)

    if request.method == "POST":
        request.user.games.remove(game)
        return redirect('profile', request.user.id)

    return render(request, 'findgame/remove.html', {"game": game})


def login_(request):
    # page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            # pass # შეცდომა
            messages.error(request,'მომხმარებლის სახელი არ არსებობს!')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'მომხმარებელი ან პაროლი არასწორია!')

    # context = {'page': page}
    return render(request, 'findgame/login.html')  # , context


def logout_(request):
    logout(request)
    return redirect('home')


def register_(request):
    form = AppUserCreationForm()

    if request.method == 'POST':
        form = AppUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) #ეგრევე მონაცემთა ბაზაში არ ვუშვებთ
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')

    context = {'form': form}
    return render(request, 'findgame/register.html', context)


def add_game(request):
    ages = Age.objects.all()
    categories = Category.objects.all()
    form = GameForm()

    if request.method == "POST":
        game_age = request.POST.get('age')
        age, created = Age.objects.get_or_create(age=game_age)

        game_category = request.POST.get('category')
        category, created = Category.objects.get_or_create(name=game_category)

        form = GameForm(request.POST, request.FILES)  # Pass files to the form

        new_game = Game(picture=request.FILES['picture'], name=form.data['name'], recommendedAges=age, equipment=form.data['equipment'],
                        numberOfPlayers=form.data['numberOfPlayers'], keyFeatures=form.data['keyFeatures'], tips=form.data['tips'],
                        description=form.data['description'], howToPlay=form.data['howToPlay'], content=request.FILES['content'],
                        creator=request.user)

        if not (Game.objects.filter(content=new_game.content) or Game.objects.filter(name=new_game.name)):
            new_game.save()  # Now save
            new_game.category.add(category)  # Add the category after saving

        return redirect('home')

    context = {'form': form, 'ages': ages, 'categories': categories}
    return render(request, 'findgame/add_game.html', context)


def reading(request, id):
    game = Game.objects.get(id=id)
    return render(request, 'findgame/reading.html', {'game': game})


def delete_game(request, id):
    game = Game.objects.get(id=id)
    if request.method == 'POST':
        game.picture.delete()
        game.content.delete()
        game.delete()
        return redirect('home')
    return render(request, 'findgame/del-game.html', {'game': game})


@login_required(login_url='login')
def update_user(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile', user.id)

    return render(request, 'findgame/update_user.html', {'form': form})