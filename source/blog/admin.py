from django.contrib import admin
from .models import BlogPost, PostComments

admin.site.register([BlogPost, PostComments])
# Register your models here.
