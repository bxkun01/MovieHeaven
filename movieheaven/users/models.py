from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user= models.OneToOneField(User, on_delete= models.CASCADE, null=True)
    image= models.ImageField(default='default.jpeg', upload_to="upload_images")


    def __str__(self):
        return f"{self.user.username}'s Profile"

