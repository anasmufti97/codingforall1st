from django.urls import path, include

from home.views import *
from home import admin



urlpatterns = [

# path('', home, name='home'),
# path('htmlPage/', htmlPage, name='htmlPage'),
# 
# 
    path('register/',UserRegistrationView.as_view(), name='register'),
    path('login/',UserLoginView.as_view(), name='login'),

]
