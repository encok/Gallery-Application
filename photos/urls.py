from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery',),
    path('photo/<str:pk>/', views.gallery, name='gallery',),
    path('', views.gallery, name="gallery",)
]