from django.urls import path, include
from .views import UserRegisterView, UserDashbordPage, ShowAllWorkers, UserProfilePage
from django.urls import re_path as url

urlpatterns = [
    path('login-and-register/', UserRegisterView.as_view(), name='login-and-register'),
    path('user-dashboard/', UserDashbordPage, name='user-dashboard'),
    path('workers-profile/', ShowAllWorkers.as_view(), name='workers-profile'),
    path('profile/<int:pk>', UserProfilePage.as_view(), name='profile'),
    # path('tailwind-dashboard/', TailwindDashboardTemplate, name='tailwind-dashboard'),
    url(r'^messages/', include('django_messages.urls')),
]
