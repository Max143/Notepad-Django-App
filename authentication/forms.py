from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from .models import profile


# User Registeration Form
class RegisterForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']



# User Profile Udpate Form
class ProfileUpdateForm(forms.ModelForm):
	bio = forms.CharField(required=False)
	location = forms.CharField(required=False)
	image = forms.ImageField(required=False)
	class Meta:
		model = profile
		fields = ['bio', 'location','image']
