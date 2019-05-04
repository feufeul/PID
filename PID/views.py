from . import models, forms
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponseRedirect, HttpResponse


def get_home(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['login'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/users')
            else:
                return HttpResponseRedirect('/?login=error')
        return HttpResponseRedirect('/?login=error2')
    else:
        context = {
            'form': forms.LoginForm()
        }
        return render(request, 'PID/home.html', context)


def get_users_name(request):
    user_manager = list(models.User.objects.all())
    context = {
        'list': user_manager
    }
    return render(request, 'PID/users.html', context)


def get_shows(request):
    show_manager = list(models.Show.objects.all())
    context = {
        "info": show_manager
    }
    # if request.session['login']:
    #     return HttpResponseRedirect('/')
    return render(request, 'PID/shows.html', context)


def get_inscription(request):
    if request.method == 'POST':
        form = forms.InscriptionForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data['login'], form.cleaned_data['email'],
                                            form.cleaned_data['password'])
            user.last_name = form.cleaned_data['last_name']
            user.first_name = form.cleaned_data['first_name']
            user.save()
            return HttpResponseRedirect('/')
    else:
        form = forms.InscriptionForm()
    return render(request, 'PID/inscription.html', {'form': form})


def get_disconnect(request):
    logout(request)
    return HttpResponseRedirect('/')
