from django.test import TestCase
from .models import BlogPost


class BlogModelTestCase(TestCase):
    def setUp(self):
        BlogPost.objects.create(title="Post Number #1", text="lorem ipsum", )

    def test_blog_post_created(self):
        firstPost = BlogPost.objects.get(id=1)
        self.assertEqual(firstPost.title, "Post Number #1")
