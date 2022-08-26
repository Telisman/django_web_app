from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail


def HomePageView(request):
    if request.method == "POST":
        fullName = request.POST.get('fullName')
        sent_email = request.POST.get('sent_email')
        message = request.POST.get('message')
        send_mail(
            fullName,
            sent_email,
            message,
            [],
        )
        return render(request, "massage_replay.html", {})
    return render(request, "homepage.html")


def LoginPage(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user-dashboard')

        else:
            return redirect('login')
    return render(request, "signin.html", {})
