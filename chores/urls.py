from .views import AddOfferPage, OfferView, ShowOffer
from django.urls import path

urlpatterns = [
    path('AddNewOffer/', AddOfferPage, name='AddNewOffer'),
    path('Offers/', OfferView, name='OfferView'),
    path('Offer/<int:pk>', ShowOffer.as_view(), name='ShowOffer'),
]
