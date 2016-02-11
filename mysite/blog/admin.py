from django.contrib import admin

# Register your models here.
from blog.models import Post #  blog/models.py

admin.site.register(Post)