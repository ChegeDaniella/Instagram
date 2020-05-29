from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_photo = models.CharField(max_length = 30)
    bio = models.CharField(max_length = 30)

class Post(models.Model):
    image = models.CharField(max_length=30)
    image_name = models.CharField(max_length = 50)
    image_caption = models.CharField(max_length = 600)
    image_profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    

