from django.contrib import admin
from .models import BlogPost, PostComments, VisitorIp

admin.site.register([BlogPost, PostComments, VisitorIp])
# Register your models here.
