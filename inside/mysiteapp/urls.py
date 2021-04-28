"""Minorproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name='home'),
    path('homepage',views.home,name='homepage'),
    path('about',views.about,name='about'),
    path('team',views.team,name='team'),
    path('ads',views.ads,name='ads'),
    path('history',views.history,name='history'),
    path('goprediction',views.goprediction,name='goprediction'),
    path('predict',views.predict,name='predict'),
    path('save_car',views.save_car,name='save_car'),
    path('getalldata',views.getalldata,name='getalldata'),
]
