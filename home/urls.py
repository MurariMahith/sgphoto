from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('index',views.index,name='index'),
    path('works',views.works,name='works'),
    path('next',views.next,name='next'),
    path('soon',views.soon,name='soon'),
    path('buy',views.buy,name='buy'),
    path('myorders',views.myorders,name='myorders'),
    path('gallery',views.gallery,name='gallery')
]