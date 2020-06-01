from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to = 'saved/' ,default="default.jpg")
    bio = models.CharField(max_length = 30)

    def __str__(self):
        return f'{self.user} Profile'

    def save_profile(self):
        self.save()

    # def save(self):
    #     img = Image.open(self.profile_photo.path)

    #     if img.height > 300 or img.width >300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.profile_photo.path)

class Post(models.Model):
    image = models.ImageField(upload_to = 'saved/')
    image_name = models.CharField(max_length = 50)
    image_caption = models.CharField(max_length = 600)
    image_profile = models.ForeignKey(User,on_delete=models.CASCADE)
    image_likes = models.ManyToManyField(User,default=None, blank=True ,related_name="image_likes")


    def __str__(self):
        return self.image_name

    class Meta:
        ordering = ['image_name']

    def save_post(self):
        self.save()

    def nun_likes(self):
        return self.image_likes.all().count()    

    def delete_post(self):
        post = self.object.filter(pk=id).delete()
        return post    
LIKE_CHOICES = (
    ('Like','Like'),
    ('Unlike','Unlike')
)

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return self.value

    def save_like(self):
        self.save()    

    
class Comments(models.Model):
    post = models.ForeignKey(Post, related_name="comments" , on_delete=models.CASCADE)
    body = models.CharField(max_length=800, null=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def save_comment(self):
        self.save()

    def __str__(self):
        return self.body 



