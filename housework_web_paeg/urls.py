from django.contrib import admin
from django.urls import path,include
from django.urls import re_path as url




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home_page.urls')),
    path('clients/', include('django.contrib.auth.urls')),
    path('clients/',include('clients.urls')),
    path('chores/', include('django.contrib.auth.urls')),
    path('chores/',include('chores.urls')),
    url(r'^messages/', include('django_messages.urls')),
]
