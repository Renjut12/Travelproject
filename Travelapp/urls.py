from django.urls import path
from . import views




urlpatterns = [

    path('',views.index,name='index'),
    path('Home',views.Home,name='Home'),
    path('Registration',views.Registration,name='Registration'),
    path('Login', views.Login,name='Login'),
    path('Logout',views.Logout,name='Logout')

]