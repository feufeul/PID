from django import forms
from PID.models import Agency
from django.contrib.auth.models import User
from PID.models import Profile


class InscriptionForm(forms.Form):
	login = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput)
	email = forms.EmailField()
	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)


class ProfileUpdateForm(forms.Form):
	password = forms.CharField(widget=forms.PasswordInput)
	email = forms.EmailField()
	first_name = forms.CharField(max_length=100)
	last_name = forms.CharField(max_length=100)


class LoginForm(forms.Form):
	login = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput)


# class InscriptionForm(forms.ModelForm):
# 	class Meta:
# 		model = Profile
# 		fields = ['first_name', 'last_name', 'email']
#
#
class ProfileForm(forms.Form):
	language = forms.CharField(max_length=100)


class SearchForm(forms.Form):
	show = forms.CharField(max_length=1000)


class CategoryForm(forms.Form):
	category = forms.CharField(max_length=10)


class ArtistForm(forms.Form):
	firstname = forms.CharField(max_length=100)
	lastname = forms.CharField(max_length=100)
	# agency = forms.IntegerField()
	agency = forms.ModelChoiceField(queryset=Agency.objects.all(), to_field_name="id")
