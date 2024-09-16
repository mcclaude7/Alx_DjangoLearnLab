from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms import ProfileForm, UserUpdateForm
from django.http import HttpResponse

# User registration view
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# User login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

# User logout view
def logout_view(request):
    logout(request)
    return redirect('login')

# User profile view
@login_required
def profile_view(request):
    return render(request, 'registration/profile.html')

@login_required
def profile_view(request):

    try:
        profile = request.user.profile
    except profile.DoesNotExist:
        return HttpResponse("Profile not found. Please create a profile.")
    
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile.html', {'form': form})
    #if request.method == 'POST':
       # user_form = UserUpdateForm(request.POST, instance=request.user)
        #profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
       # if user_form.is_valid() and profile_form.is_valid():
        #    user_form.save()
         #   profile_form.save()
          #  return redirect('profile')
    #else:
     #   user_form = UserUpdateForm(instance=request.user)
      #  profile_form = ProfileForm(instance=request.user.profile)
    #return render(request, 'registration/profile.html', {'user_form': user_form, 'profile_form': profile_form})
