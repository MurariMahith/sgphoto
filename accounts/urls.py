from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout,name='logout'),
    path('checkadmin',views.checkadmin,name='checkadmin'),
    path('adminbypass',views.adminbypass,name='users'),
    path('users',views.users,name='users'),
    path('forgotpassword',views.forgotpassword, name='forgotpassword')
]