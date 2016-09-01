from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import (LoginForm)


def index(request):
    return render(request, "index.html", locals())


def log_in(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("website:index"))
            else:
                error = "Invalid username or password"
    return render(request, "auth/login.html", locals())


def register(request):
    return render(request, "auth/register.html", locals())
