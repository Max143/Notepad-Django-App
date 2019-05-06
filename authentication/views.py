from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, ProfileUpdateForm
from django.contrib.auth.models import User
import datetime
from django.contrib import messages
from .models import profile
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Registering New User
# Counting the number of account created 
# Notifying in Terminal window
count = 0
def RegisterView(request):
	global count
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password1 = form.cleaned_data['password1']
			password2 = form.cleaned_data['password2']

			user = form.save()
			messages.success(request, 'Account Created Successfully')
			
			# For terminal 
			print('New Account Created - {}'.format(datetime.datetime.now()))
			count += 1
			print('Total Actice User Accounts: ', count)
			return redirect('notepadview')
	else:
		form = RegisterForm()
		context = {'form': form}
	return render(request, 'registration/register.html', context)



# Profile View
def ProfileView(request):
	#user =get_object_or_404(profile, username=username)
	#args = {'user': user}
	return render(request, 'registration/profile.html')


# Edit View
@login_required
def EditProfile(request, id=None):
	
	if request.method == 'POST':
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
		if p_form.is_valid():
			bio = p_form.cleaned_data['bio']
			location = p_form.cleaned_data['location']
			image = p_form.cleaned_data['image']

			profile = p_form.save(commit=False)
			profile.user = request.user
			profile.save()

			messages.success(request, f'Profile Update Successfully!')
			return redirect('profile')
	else:
		p_form = ProfileUpdateForm()
		context = {'p_form': p_form}
	return render(request, 'registration/editprofile.html', context)
'''
Error: 
Django NOT NULL constraint failed userprofile.user_id in case of uploading a file

Means:


---------------------------------------------------------------------------------------




Exception Type:	IntegrityError
Exception Value:	
UNIQUE constraint failed: authentication_profile.user_id

Means: 

It's not strange. You already have a profile for that user, 
so adding another one breaks the unique constraint. You need to edit the existing one, 
not add a new one.
------------------------------------------------------------------------------------


0.
 

models.py....
class UserProfile(models.Model):
    user = models.ForeignKey(User, related_name='uploaded_by')
    names = models.CharField(max_length=40)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    uploads = models.FileField(upload_to= 'blablabla')


Problem Here: 
I must say your model looks a bit odd; 
you have multiple profiles for each user, each with a single upload. 
Seems more likely you want a single profile, with a OneToOne relationship to User, 
than a separate Uploads model with a ForeignKey to UserProfile.

'''


# User List View
def UserListView(request):
	user_list = User.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(user_list, '3')
	try:
		users = paginator.page(page)
	except PageNotAnInteger:
		users = paginator.page(1)
	except EmptyPage:
		users = paginator.page(paginator.num_pages)
	return render(request, 'registration/userlist.html', { 'users': users })
	  	
'''
# Class-Based View also ease the use of paginator
class UserListView(ListView):
    model = User
    template_name = 'core/user_list.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'users'  # Default: object_list
    paginate_by = 10
    queryset = User.objects.all()  # Default: Model.objects.all()



 '''