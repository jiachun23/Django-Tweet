"""app1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url,include
from django.views.generic.base import RedirectView
from tweet import views
from tweet.views import TweetListView

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.TweetListView.as_view(),name='home'),
    url(r'^special/',views.special,name='special'),
    url(r'^tweet/',include('tweet.urls')),
    url(r'^logout/$', views.user_logout, name='logout')
]