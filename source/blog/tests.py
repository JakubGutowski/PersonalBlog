from django.test import TestCase, Client
from django.shortcuts import render
from .models import BlogPost, VisitorIp



class BlogModelTestCase(TestCase):
    def setUp(self):
        BlogPost.objects.create(title="Post Number #1", text="lorem ipsum", )

    def test_blog_post_created(self):
        firstPost = BlogPost.objects.get(id=1)
        firstPost.save()
        self.assertEqual(firstPost.title, "Post Number #1")


class MainPageTestCase(TestCase):
    def setUp(self):
        first = BlogPost.objects.create(title="Post Number #1", text="lorem ipsum", )
        self.client = Client()
        self.response = self.client.get('/')

    def test_main_page_status(self):
        self.assertEqual(self.response.status_code, 200)

    def test_main_page_rendered_html(self):
        posts_on_page = self.response.context['latest_posts']
        self.assertEqual(posts_on_page[0], BlogPost.objects.get(id=1))

    def test_main_page_ip_loging(self):
        self.assertEqual(len(VisitorIp.objects.all()), 1)
        self.response = self.client.get('/')
        self.assertEqual(len(VisitorIp.objects.all()), 2)
