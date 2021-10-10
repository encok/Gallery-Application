from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('', views.viewAbout, name='viewAbout'),
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    path('add/', views.addPhoto, name='add'),
]