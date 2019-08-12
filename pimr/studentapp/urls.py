from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('calcsi', views.si, name='si'),
    path('add', views.add, name='add'),
    path('addlogic', views.addlogic, name='addlogic')
]
