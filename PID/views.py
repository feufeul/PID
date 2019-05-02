from django.views.generic import TemplateView
from django.http import HttpResponse
from . import manager
from django.shortcuts import render


class HomePageView(TemplateView):
    template_name = 'PID/home.html'


def get_users_name(request):
    user_manager = manager.UserManager()
    list = []
    for e in user_manager.all_user():
        list.append(e)
    context = {
        'list': list
    }
    return render(request, 'PID/users.html', context)


def get_shows(request):
    show_manager = manager.ShowManager().all_show()
    info = {}
    i = 1
    for item in show_manager:
        info.update({i: item})
        i += 1
    # context = {i: show_manager[i] for i in range(0, len(show_manager))}
    # shows = []
    # urls = []
    # prices = []
    # bookables = []
    # for e in show_manager:
    #     shows.append(e[1])
    #     urls.append(e[2])
    #     prices.append(e[3])
    #     bookables.append(e[4])
    # context = {
    #     'shows': shows,
    #     'urls': urls,
    #     'prices': prices,
    #     'bookables': bookables
    # }
    context ={
        "info": info
    }
    return render(request, 'PID/shows.html', context)
