from django.contrib import admin
from django.urls import path, include
from django.urls import re_path as url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include('home_page.urls')),
                  path('clients/', include('django.contrib.auth.urls')),
                  path('clients/', include('clients.urls')),
                  path('chores/', include('django.contrib.auth.urls')),
                  path('chores/', include('chores.urls')),
                  url(r'^messages/', include('django_messages.urls')),
                  path("__reload__/", include("django_browser_reload.urls")),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
