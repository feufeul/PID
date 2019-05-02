from django.views.generic import TemplateView
from . import manager, models
from django.shortcuts import render


class HomePageView(TemplateView):
    template_name = 'PID/home.html'


def get_users_name(request):
    user_manager = list(models.User.objects.all())
    context = {
        'list': user_manager
    }
    return render(request, 'PID/users.html', context)


def get_shows(request):
    show_manager = list(models.Show.objects.all())
    context ={
        "info": show_manager
    }
    return render(request, 'PID/shows.html', context)
