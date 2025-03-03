# Generated by Django 5.1.6 on 2025-02-28 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('release_date', models.DateField()),
                ('genre', models.CharField(max_length=100)),
                ('poster', models.ImageField(upload_to='movie_posters/')),
            ],
        ),
    ]
