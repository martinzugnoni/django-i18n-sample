from django.urls import path, include
from django.views.generic.base import TemplateView
from core import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('about-us', views.about_page, name='about-us'),
]
