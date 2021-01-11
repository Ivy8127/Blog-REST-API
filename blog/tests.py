from django.test import TestCase
from .models import Posts


class PosttestCase(TestCase):
    """Defines the test suite for the Post model

    Args:
        TestCase ([type]): [description]
    """
    def setUp(self):
        """Used to set up classes and objects /instantiating objects
        """
        self.title = 'Django rest'
        #create post object
        self.post = Posts(title = self.title)


    def test_model_can_create_a_post(self):
        """Tests whether the post model can create posts
        """
        #count the original number of posts
        old_count = Posts.objects.count()
        #save it
        self.post.save()
        #count the new number of posts when a post has been added
        new_count = Posts.objects.count()
        #assert that they are not equal , if true then the model can create a posts
        self.assertNotEqual(old_count, new_count)   
