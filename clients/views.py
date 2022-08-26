from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse_lazy
from .forms import SingUpForm, UserSettings
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from clients.models import ClientsUsers
import urllib.request
import json
import requests
import datetime
from clients.filters import FilterUser


def UserDashbordPage(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=16afaa2e90dcdea0eaa852fc47782ac2'
    city = 'Belgrade'
    city_weather = requests.get(url.format(city)).json()  # request the API data and convert the JSON
    current_date_time = datetime.datetime.now()
    weather = {
        'city': city,
        'temperature': city_weather['main']['temp'],
        'description': city_weather['weather'][0]['description'],
        'icon': city_weather['weather'][0]['icon']
    }
    context = {'weather': weather,
               'current_date_time': current_date_time,
               }

    return render(request, 'dashboard.html', context)  # returns the index.html template


class UserRegisterView(generic.CreateView):
    form_class = SingUpForm
    template_name = 'sign-up.html'
    success_url = reverse_lazy('housemaster')


def ShowAllWorkers(request):
    workers = ClientsUsers.objects.all()
    listing_filter = FilterUser(request.GET, queryset=workers)
    context = {
        'listing_filter': listing_filter,
    }
    return render(request, "workers_profile.html", context)


class UserProfilePage(DetailView):
    model = ClientsUsers
    context_object_name = "workers"
    template_name = "user_detail_profile.html"

    def get_context_data(self, *args, **kwargs):
        context = super(UserProfilePage, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(ClientsUsers, pk=self.kwargs['pk'])
        return context


class Settings(generic.UpdateView):
    form_class = UserSettings
    template_name = 'user_settings.html'
    success_url = reverse_lazy('user-dashboard')

    def get_object(self):
        return self.request.user
