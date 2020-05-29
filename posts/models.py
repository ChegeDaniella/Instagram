from django.db import models

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = 'saved/')
    bio = models.CharField(max_length = 30)

class Post(models.Model):
    image = models.ImageField(upload_to = 'saved/')
    image_name = models.CharField(max_length = 50)
    image_caption = models.CharField(max_length = 600)
    image_profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    

