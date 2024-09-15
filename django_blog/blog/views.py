from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm
#from django.contrib.auth.forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
#from django.contrib import messages
#from .forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Replace 'login' with the correct URL name
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'profile.html')
    #if request.method == 'POST':
     #   user_form = UserUpdateForm(request.POST, instance=request.user)
      #  profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

#        if user_form.is_valid() and profile_form.is_valid():
 #           user_form.save()
  #          profile_form.save()
   #         messages.success(request, 'Your profile has been updated!')
    #        return redirect('profile')
    #else:
     #   user_form = UserUpdateForm(instance=request.user)
      #  profile_form = ProfileUpdateForm(instance=request.user.profile)

    #context = {
 #       'user_form': user_form,
  #      'profile_form': profile_form
   # }

    #return render(request, 'profile.html', context)

class LoginView(LoginView):
    template_name = 'login.html'

#def product(request):
    #return render(request, "base.html")

def index(request): 
    return render(request, "index.html")