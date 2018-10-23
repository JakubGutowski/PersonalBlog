from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .forms import PostComent as PostComentForm
from django.http import HttpResponse
from datetime import datetime
from calendar import month_name

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
        post = BlogPost.objects.order_by('-pubDate')
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
        form = PostComentForm(request.POST)
        context = {
            'blogpost': post,
            'comments': comments,
            'form': form,
            }
        return HttpResponse(render(request, 'postPage.html', context))

    @staticmethod
    def post(request, blogpost_id):
        form = PostComentForm(request.POST)
        if form.is_valid():
            nick = form.cleaned_data['nick']
            comment = form.cleaned_data['comment']
            postComent = PostComments()
            postComent.nick = nick
            postComent.comment = comment
            postComent.pubDate = datetime.now()
            postComent.post = BlogPost.objects.get(id=blogpost_id)
            postComent.save()
            return HttpResponseRedirect('/post/' + str(blogpost_id))


class MonthStats(View):
    @staticmethod
    def get(request, year, month):
        barChart = "visitsChart" + str(month) + str(year)
        title = "Number of visits in " + month_name[int(month)] + " " + str(year)
        context = {
            'barChart': barChart,
            'title': title,
            'date': month_name[int(month)] + " " + str(year),
        }
        return HttpResponse(render(request, 'monthStats.html', context))
