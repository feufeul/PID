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
from django.urls import path, include
from PID import views
from django.contrib import admin

urlpatterns = [
    path('', views.get_home, name='home'),
    path('disconnect/', views.get_disconnect, name='disconnect'),
    path('users/', views.get_users_name, name='users'),
    path('shows/', views.get_shows, name='shows'),
    path('inscription/', views.get_inscription, name='inscription'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]