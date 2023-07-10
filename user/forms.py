from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class UserRegisterForm(UserCreationForm):
  email = forms.EmailField(required=True)

  class Meta:
    model = User
    fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    labels = {
      'username': ('Username'),
      'first_name': ('First Name'),
      'last_name': ('Last Name'),
      'email': ('Email'),
      'password1': ('Password'),
      'password2': ('Confirm Password'),
    }


  def save(self, commit=True):
    user = super(UserRegisterForm, self).save(commit=False)
    user.email = self.cleaned_data['email']
    if commit:
      user.save()
    return user 
