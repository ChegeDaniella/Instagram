from django.test import TestCase
from .models import Post,Profile,Comments

# Create your tests here.
class profileTestModel(TestCase):
    def setUp(self):
        self.new_profile=Profile(profile_photo = 'default.jpg', bio = "This is a test")
class PostTestModel(TestCase):

    def setUp(self):
        self.new_profile=Profile(profile_photo = 'default.jpg', bio = "This is a test")
        self.new_profile.save_profile()

        self.new_comment = Comments(comments = "This is a comment")
        self.new_comment.save_comment()

        self.new_post = Post(image = "default.jpg",image_name="test image",image_caption="This is a caption",image_profile = self.new_profile , image_comments=self.new_comment)
        self.new_post.save_post()

    def test_instance_post(self):
        self.assertTrue(isinstance(self.new_post,Post))

    def tearDown(self):
        Post.objects.all().delete()    
        Comments.objects.all().delete()
        Profile.objects.all().delete()   

    def test_save_post(self):
        self.new_post.save_post()
        
            
