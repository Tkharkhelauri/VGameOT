# Generated by Django 5.0.6 on 2024-07-07 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('findgame', '0002_category_remove_game_category_alter_user_games_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='name',
        ),
    ]