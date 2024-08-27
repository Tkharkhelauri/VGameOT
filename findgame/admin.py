from django.contrib import admin
from .models import Game, Age, User, Category, Comment

# Register your models here.
#ადმინის პანელში ჩვენი შექმნილი მოდელების გამოჩენა
admin.site.register(Game)
admin.site.register(Age)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Comment)
