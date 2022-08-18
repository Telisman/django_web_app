from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from .forms import SingUpForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from clients.models import ClientsUsers


def UserDashbordPage(request):
    return render(request, "dashboard.html", {})


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
