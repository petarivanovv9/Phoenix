from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import (LoginForm, RegisterForm)
from .decorators import anonymous_required


def index(request):
    return render(request, "index.html", locals())


@anonymous_required(redirect_url=reverse_lazy('website:index'))
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
                return redirect(reverse('website:index'))
            else:
                error = "Invalid username or password"
    return render(request, "auth/login.html", locals())


@anonymous_required(redirect_url=reverse_lazy('website:index'))
def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        if request.POST.get("password", "") != request.POST.get("password2", ""):
            error = "Incorrect passwords"
            return render(request, "auth/register.html", locals())
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('website:index'))
    return render(request, "auth/register.html", locals())


@login_required
def log_out(request):
    logout(request)
    return redirect(reverse('website:index'))
