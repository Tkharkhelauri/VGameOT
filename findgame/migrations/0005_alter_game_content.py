# Generated by Django 5.0.6 on 2024-07-16 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('findgame', '0004_alter_game_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='content',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
