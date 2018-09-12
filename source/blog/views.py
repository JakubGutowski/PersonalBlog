from django.views.generic import ListView
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from .models import BlogPost, PostComments


class BlogPage(ListView):
    template_name = 'blogPage.html'
    context_object_name = 'latest_posts'

    def get_queryset(self):
        return BlogPost.objects.order_by('-pubDate')[:5]


class PostDetail(View):
    @staticmethod
    def get(request, blogpost_id):
        post = BlogPost.objects.get(id=blogpost_id)
        comments = PostComments.objects.filter(post=blogpost_id)
        context = {
            'blogpost': post,
            'comments': comments,
            }
        return HttpResponse(render(request, 'postPage.html', context))





