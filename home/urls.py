from django.urls import path, include
from home.views import *
from home import admin

urlpatterns = [

    path('register/',UserRegistrationView.as_view(), name='register'),
    path('login/',UserLoginView.as_view(), name='login'),

]
