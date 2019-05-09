from . import models, forms
from PID.forms import InscriptionForm, LoginForm
from PID.models import Profile
from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


def get_home(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
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
			'form': LoginForm()
		}
		return render(request, 'PID/home.html', context)


def get_users_name(request):
	user_manager = list(User.objects.all())
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


def get_disconnect(request):
	logout(request)
	return HttpResponseRedirect('/')
