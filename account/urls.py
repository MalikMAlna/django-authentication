from django.urls import path
from account import views

urlpatterns = [
    path('',
         views.index,
         name='homepage'),
    path('register/',
         views.registration_view,
         name='register'),
    path('logout/',
         views.logoutview,
         name='logout'),
    path('login/',
         views.loginview,
         name='login'),

]
