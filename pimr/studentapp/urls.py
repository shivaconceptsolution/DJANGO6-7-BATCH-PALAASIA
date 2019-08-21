from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='index'),
    path('reg', views.reg, name='reg'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('calcsi', views.si, name='si'),
    path('add', views.add, name='add'),
    path('addlogic', views.addlogic, name='addlogic'),
    path('viewstudent', views.viewstudent, name='viewstudent'),
    path('editstu', views.editstu, name='editstu'),
    path('deletestu', views.deletestu, name='deletestu'),
    path('updatestu', views.updatestu, name='updatestu')
]
