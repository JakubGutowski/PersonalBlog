from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from datetime import datetime

from .models import BlogPost, PostComments, VisitorIp


def collectVisitorIP(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        ipaddress = x_forwarded_for.split(',')[-1].strip()
    else:
        ipaddress = request.META.get('REMOTE_ADDR')
    get_ip = VisitorIp()  # imported class from model
    get_ip.ip_address = ipaddress
    get_ip.pub_date = datetime.now()
    get_ip.save()


class BlogPage(View):

    @staticmethod
    def get(request):
        post = BlogPost.objects.order_by('-pubDate')[:5]
        collectVisitorIP(request)

        context = {
            'latest_posts': post,

        }
        return HttpResponse(render(request, 'blogPage.html', context))

class PostDetail(View):
    @staticmethod
    def get(request, blogpost_id):
        post = BlogPost.objects.get(id=blogpost_id)
        comments = PostComments.objects.filter(post=blogpost_id)
        collectVisitorIP(request)

        context = {
            'blogpost': post,
            'comments': comments,
            }
        return HttpResponse(render(request, 'postPage.html', context))





