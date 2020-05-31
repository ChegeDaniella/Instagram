from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to = 'saved/')
    bio = models.CharField(max_length = 30)

    def __str__(self):
        return f'{self.user}Profile'

    def save_profile(self):
        self.save()

class Comments(models.Model):
    comments = models.CharField(max_length = 200)    
    def __str__(self):
        return f'{self.comments} Comments'  

    def save_comment(self):
        self.save()

    

class Post(models.Model):
    image = models.ImageField(upload_to = 'saved/')
    image_name = models.CharField(max_length = 50)
    image_caption = models.CharField(max_length = 600)
    image_profile = models.ForeignKey(User,on_delete=models.CASCADE)
    image_likes = models.IntegerField(default=0)
    image_comments = models.ForeignKey(Comments, on_delete=models.CASCADE)

    def __str__(self):
        return self.image_name

    class Meta:
        ordering = ['image_name']

    def save_post(self):
        self.save()

    def delete_post(self):
        post = self.object.filter(pk=id).delete()
        return post    

    

