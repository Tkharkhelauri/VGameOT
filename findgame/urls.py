from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('games/<str:id>/', views.game_description, name='game_description'),
    path('adding/<str:id>/', views.adding, name='adding'),
    path('remove/<str:id>/', views.remove, name='remove'),
    path('login/', views.login_, name='login'),
    path('register/', views.register_, name='register'),
    path('logout/', views.logout_, name='logout'),
    path('upload/', views.add_game, name='upload'),
    path('delete_game/<str:id>', views.delete_game, name='delete_game'),
    path('reading/<str:id>/', views.reading, name='reading'),
    path('update_user/', views.update_user, name='update_user'),
    path('delete_comment/<str:id>', views.delete_comment, name='delete_comment')

]