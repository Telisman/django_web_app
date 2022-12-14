from django.urls import path, include
from .views import UserRegisterView, UserDashbordPage, ShowAllWorkers, UserProfilePage, Settings, AddUserWorkExperience, \
    AddEducation
from django.urls import re_path as url

urlpatterns = [
    path('login-and-register/', UserRegisterView.as_view(), name='login-and-register'),
    path('user-dashboard/', UserDashbordPage, name='user-dashboard'),
    path('addwork/', AddUserWorkExperience, name='addwork'),
    path('addeducation/', AddEducation, name='addeducation'),
    path('workers-profile/', ShowAllWorkers, name='workers-profile'),
    path('profile/<int:pk>', UserProfilePage.as_view(), name='profile'),
    path('settings/>', Settings.as_view(), name='settings'),
    url(r'^messages/', include('django_messages.urls')),
]
