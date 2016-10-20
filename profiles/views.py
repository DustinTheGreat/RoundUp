from django.shortcuts import render
from .models import UserProfile
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/account/login/')
def profile_view(request):
	instance = UserProfile.objects.get(user=request.user)
	return render(request, 'profiles/profile.html',{'instance':instance})
def all_profile_view(request, id):
	instance = UserProfile.objects.get(user_id= id)
	return render(request, 'profiles/profile.html',{'instance':instance})