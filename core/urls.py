
from django.contrib import admin
from django.urls import path, include

# from home.views import *

urlpatterns = [

# path('', home, name='home'),
# path('htmlPage/', htmlPage, name='htmlPage'),

    path('admin/', admin.site.urls),
    path('api/user/', include('home.urls')),
]
