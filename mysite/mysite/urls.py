"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255) 
    datetime = models.DateTimeField(u'd') 
    content = models.TextField(max_length=10000) 
            
                def __unicode__(self):
                        return self.title
                        
                            def get_absolute_url(self):
                                    return "/blog/%i/" % self.id