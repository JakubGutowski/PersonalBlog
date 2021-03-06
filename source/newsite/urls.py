"""newsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, path
from blog.views import BlogPage, PostDetail, MonthStats


urlpatterns = [
    re_path(r'^$' , BlogPage.as_view(), name='blog'),
    re_path(r'^admin/', admin.site.urls, name='admin',),
    path('post/<int:blogpost_id>', PostDetail.as_view(), name='post'),
    path('stats/<str:year>/<str:month>', MonthStats.as_view(), name='stats')
]
