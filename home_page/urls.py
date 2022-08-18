from django.urls import path, include
from .views import HomePageView, LoginPage

urlpatterns = [
    path('Housemaster/', HomePageView, name='housemaster'),
    path('Housemaster/SingIn', LoginPage, name='sing-in'),
]
