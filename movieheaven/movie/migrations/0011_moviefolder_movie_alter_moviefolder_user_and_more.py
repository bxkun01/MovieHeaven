# Generated by Django 5.1.6 on 2025-03-10 07:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0010_alter_moviefolder_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='moviefolder',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='folders', to='movie.movie'),
        ),
        migrations.AlterField(
            model_name='moviefolder',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='folders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='moviefolder',
            unique_together={('user', 'movie')},
        ),
    ]
