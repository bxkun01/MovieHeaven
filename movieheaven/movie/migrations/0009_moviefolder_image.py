# Generated by Django 5.1.6 on 2025-03-10 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0008_moviefolder_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviefolder',
            name='image',
            field=models.ImageField(blank=True, default='default_folder.png', upload_to='folder_image'),
        ),
    ]
