from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.photo_of_day,name = 'photoToday'),
    url('^today/$',views.photo_of_day,name='photoToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_photo,name = 'pastPhoto'),
    url(r'^search/', views.search_results, name='search_results')  
]