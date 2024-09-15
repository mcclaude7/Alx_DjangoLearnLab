#from django import forms
#from django.contrib.auth.models import User
#from .models import Profile

#class UserUpdateForm(forms.ModelForm):
 #   email = forms.EmailField()

#    class Meta:
 #       model = User
  #      fields = ['username', 'email']

#class ProfileUpdateForm(forms.ModelForm):
 #   class Meta:
  #      model = Profile
   #     fields = ['bio', 'profile_picture', 'date_of_birth']



from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
