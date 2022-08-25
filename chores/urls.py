from .views import AddOfferPage, OfferView, ShowOffer
from django.urls import path, re_path, include

urlpatterns = [
    path('AddNewOffer/', AddOfferPage, name='AddNewOffer'),
    path('Offers/', OfferView, name='OfferView'),
    path('Offer/<int:pk>', ShowOffer.as_view(), name='ShowOffer'),
    # path('search_venues/', search_venues, name='searchvenues'),
]
