from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from .forms import SingUpForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from clients.models import ClientsUsers

def UserDashbordPage(request):
    return render(request,"user_dashboard_page.html",{})

class UserRegisterView(generic.CreateView):
    form_class = SingUpForm
    template_name = 'login_and_register_form.html'
    success_url = reverse_lazy('housemaster')


class ShowAllWorkers(ListView):
    model = ClientsUsers
    context_object_name = "workers"
    template_name = 'workers_profile.html'

    def get_queryset(self):
        return ClientsUsers.objects.filter(user_type=ClientsUsers.worker)
