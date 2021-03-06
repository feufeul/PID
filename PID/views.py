from . import models, forms
from PID.forms import LoginForm
from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from PID.filter import ShowFilter
from PID.models import Show, Agency, Artist
from django.shortcuts import redirect
import requests
import json


def get_home(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user = authenticate(username=form.cleaned_data['login'], password=form.cleaned_data['password'])
			if user is not None:
				login(request, user)
				return HttpResponseRedirect('/')
			else:
				return HttpResponseRedirect('/?login=error')
		return HttpResponseRedirect('/?login=error2')
	else:
		context = {
			'form': LoginForm()
		}
		return render(request, 'PID/home.html', context)


def get_users_name(request):
	if not request.user.is_authenticated:
		return redirect('/')
	if not request.user.is_superuser:
		return HttpResponseRedirect('/?unauthorized=true')
	user_manager = list(User.objects.all())
	context = {
		'list': user_manager
	}
	return render(request, 'PID/users.html', context)


def get_shows(request):
	shows_list = Show.objects.all()
	filtered = ShowFilter(request.GET, shows_list)
	show_manager = filtered.qs
	paginator = Paginator(show_manager, 5)
	page = request.GET.get('page')
	shows = paginator.get_page(page)
	context = {
		"info": shows,
		"filter": filtered
	}
	return render(request, 'PID/shows.html', context)


def get_sorted_shows(request):
	shows_list = Show.objects.all().order_by(request.GET.get('sort'))
	show_manager = list(shows_list)
	paginator = Paginator(show_manager, 5)
	page = request.GET.get('page')
	shows = paginator.get_page(page)
	context = {
		"info": shows
	}
	return render(request, 'PID/sorted_shows.html', context)


def get_inscription(request):
	if not request.user.is_authenticated:
		return redirect('/')
	if request.method == 'POST':
		form = forms.InscriptionForm(request.POST)
		profile_form = forms.ProfileForm(request.POST)
		if form.is_valid() and profile_form.is_valid():
			user = User.objects.create_user(form.cleaned_data['login'], form.cleaned_data['email'],
											form.cleaned_data['password'])
			user.last_name = form.cleaned_data['last_name']
			user.first_name = form.cleaned_data['first_name']
			# profile = Profile(user, form.cleaned_data['language'])
			# profile.user = user
			user.profile.language = profile_form.cleaned_data['language']
			user.save()
			# profile.save()
			return HttpResponseRedirect('/')
	else:
		form = forms.InscriptionForm()
		profile_form = forms.ProfileForm()
	return render(request, 'PID/inscription.html', {'form': form, 'profile_form': profile_form})


def get_api_shows(request):
	if not request.user.is_authenticated:
		return redirect('/')
	if not request.user.is_superuser:
		return HttpResponseRedirect('/?unauthorized=true')
	url_begin = "https://www.theatre-contemporain.net/api/spectacles/"
	url_end = "?k=691202053ce0b5156cc95a44a224c3c300f49f67"
	if request.method == 'POST':
		form = forms.SearchForm(request.POST)
		if form.is_valid():
			req = requests.get(url_begin + form.cleaned_data['show'] + url_end)
			decoded_json = json.loads(req.text)
			data = {"items": decoded_json}
			return render(request, 'PID/api_render.html', data)
	else:
		form = forms.SearchForm()
	return render(request, 'PID/api_shows.html', {'form': form})


def get_disconnect(request):
	logout(request)
	return HttpResponseRedirect('/')


def get_category(request):
	category_manager = list(models.Category.objects.all())
	show_manager = list(models.Show.objects.all())
	form = forms.CategoryForm()
	context = {
		"cat": category_manager,
		"show": show_manager,
		"form": form
	}
	if request.method == 'POST':
		form = forms.CategoryForm(request.POST)
		if form.is_valid():
			cat = models.Category()
			cat.type = form.cleaned_data['type']
			cat.save()
			return HttpResponseRedirect('/')
	return render(request, 'PID/category.html', context)


def get_category_id(request, id):
	show_manager = list(models.Show.objects.all().filter(category_id=id))
	context = {
		"show": show_manager
	}
	return render(request, 'PID/category2.html', context)


def get_profile_id(request):
	if not request.user.is_authenticated:
		return redirect('/')
	# print(request.user)
	if request.method == 'POST':
		form = forms.ProfileUpdateForm(request.POST)
		if form.is_valid():

			user = User.objects.get(username=request.user)
			user.last_name = form.cleaned_data['last_name']
			user.first_name = form.cleaned_data['first_name']
			user.set_password(form.cleaned_data['password'])
			user.email = form.cleaned_data['email']
			user.save()
			return HttpResponseRedirect('/')
	else:
		form = forms.ProfileUpdateForm()
		profile_manager = list(models.User.objects.all().filter(username=request.user))
		context = {
			"profiles": profile_manager,
			"form": form
		}
	return render(request, 'PID/profile.html', context)


def get_agencies(request):
	agencies = Agency.objects.all()
	artists = Artist.objects.all()
	return render(request, 'PID/agencies.html', context={"agencies": agencies, "artists": artists})


def get_agencies_by_id(request, id):
	agency = Agency.objects.get(pk=id)
	artists = Artist.objects.filter(agency_id=id)
	return render(request, 'PID/agencies_2.html', context={"agency": agency, "artists": artists})


def get_artists(request):
	artists = Artist.objects.all()
	form = forms.ArtistForm()
	context = {"artists": artists, "form": form}
	if request.method == 'POST':
		form = forms.ArtistForm(request.POST)
		if form.is_valid():
			artist = Artist.objects.create()
			artist.firstname = form.cleaned_data['firstname']
			artist.lastname = form.cleaned_data['lastname']
			artist.agency_id = form.cleaned_data['agency']
			artist.save()
			return render(request, 'PID/artists.html', context)
	return render(request, 'PID/artists.html', context)
