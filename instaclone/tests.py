from django.test import TestCase

from .models import Image, Profile, Comment, Instalikes

# Create your tests here.
class TestImageClass(TestCase):
    '''Set up test object'''
    def setUp(self):

        '''creating a new profile and saving it'''
        self.profile = Profile(profile_photo="", bio="Potato lover")
        self.profile.save_profile()

        '''creating a new post and saving it'''
        self.image = Image(image ="" , image_name = "nice", image_caption="This seems okay" ,likes = "10", comments = "It worked alright")
        self.image.save()
    
        self.comment = Comment, comment="This is nice")
        self.comment.save()

        self.Instalikes = Instalike(post=self.Image,)
        self.Instalikes.save()

    def tearDown(self):
        Image.objects.all().delete()
        Profile.objects.all().delete()
        Comment.objects.all().delete()
        Instalikes.objects.all().delete()

    '''Test to check instance created'''
    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))
