from django.contrib import admin
from .models import Movie, Comment, MovieFolder

admin.site.register(Movie)
admin.site.register(Comment)
admin.site.register(MovieFolder)