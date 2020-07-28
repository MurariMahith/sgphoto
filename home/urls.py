from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('',views.home,name='home'),
    path('index',views.index,name='index'),
    path('works',views.works,name='works'),
    path('next',views.next,name='next'),
    path('soon',views.soon,name='soon'),
    path('buy',views.buy,name='buy'),
    path('myorders',views.myorders,name='myorders'),
    path('gallery',views.gallery,name='gallery'),
    path('search',views.search,name='search'),
    path('news_feed',views.news_feed,name='news_feed'),
    path('post_feed',views.post_feed,name='post_feed')
]