"""PID URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path, include
from PID import views
from PID.models import Show
from django.contrib import admin
from django_filters.views import FilterView

urlpatterns = [
    path('', views.get_home, name='home'),
    path('disconnect/', views.get_disconnect, name='disconnect'),
    path('users/', views.get_users_name, name='users'),
    url(r'^shows/', views.get_shows, name='shows'),
    url(r'^sorted_shows/', views.get_sorted_shows, name='sorted_shows'),
    # path('search_show/', views.get_filtered_shows, name='search_shows'),
    path('inscription/', views.get_inscription, name='inscription'),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('api_shows/', views.get_api_shows, name='api_shows'),
    path('api_render/', views.get_api_shows, name='api_render'),
    path('category/', views.get_category, name='categorie'),
    path('category/<int:id>', views.get_category_id),
    path('profile/', views.get_profile_id, name='profile')
]