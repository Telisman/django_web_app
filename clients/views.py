from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from .forms import SingUpForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from clients.models import ClientsUsers
import urllib.request
import json
import requests
import datetime


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
    # return render(request, "dashboard.html", {})


class UserRegisterView(generic.CreateView):
    form_class = SingUpForm
    template_name = 'sign-up.html'
    success_url = reverse_lazy('housemaster')


class ShowAllWorkers(ListView):
    model = ClientsUsers
    context_object_name = "workers"
    template_name = 'workers_profile.html'

    def get_queryset(self):
        return ClientsUsers.objects.filter(user_type=ClientsUsers.worker)


#
# def TailwindDashboardTemplate(request):
#     return render(request, "index.html", {})

6


class UserProfilePage(DetailView):
    model = ClientsUsers
    template_name = "profile.html"

    def get_context_data(self, *args, **kwargs):
        context = super(UserProfilePage, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(ClientsUsers, pk=self.kwargs['pk'])
        return context
