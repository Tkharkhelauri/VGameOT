from django.contrib.auth.forms import UserCreationForm
from .models import User, Game, Age, Category
from django import forms
from django.forms import ModelForm  #როცა ჩვენ მოდელებს ვქმნით


class AppUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class GameForm(forms.ModelForm):
    age = forms.ModelChoiceField(queryset=Age.objects.all())
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Game
        fields = '__all__'
