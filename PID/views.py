from django.views.generic import TemplateView
from django.http import HttpResponse
from . import manager


class HomePageView(TemplateView):
    template_name = 'PID/home.html'


def current_datetime(request):
    user_manager = manager.UserManager()
    html = "<html><body>"
    for e in user_manager.all_user():
        html += "<div>"
        html += e
        html += "</div>"
    # html += "blah"
    html += "</body></html>"
    return HttpResponse(html)
