from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Game, Age, Category
from django import forms
from django.forms import ModelForm  #როცა ჩვენ მოდელებს ვქმნით



class UserUpdateForm(UserChangeForm):
    password = forms.CharField(widget=forms.PasswordInput(), required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'bio', 'avatar', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bio'].label = 'ბიოგრაფია'
        self.fields['password'].label = 'პაროლი (შეავსეთ მხოლოდ ცვლილების შემთხვევაში)'




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


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'username', 'email', 'bio', 'games']
        labels = {
            'avatar': 'ავატარი',
            'username': 'მომხმარებლის სახელი',
            'email': 'ელ. ფოსტა',
            'bio': 'ბიოგრაფია',
            'games': 'თამაშები'
        }