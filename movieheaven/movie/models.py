from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title= models.CharField(max_length=200)
    description= models.TextField()
    release_date = models.DateField()
    genre = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='movie_posters/')

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,related_name="comments", on_delete=models.CASCADE) 
    text = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-created_at']

    def __str__(self):
        return f"Comment by {self.user.username} on {self.movie.title}"

class MovieFolder(models.Model):
    user= models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title= models.CharField(max_length=300)
    created_at= models.DateField(auto_now_add=True)


    
    