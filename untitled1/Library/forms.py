from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from Library.models import Author, Book, BookInstance, Publisher, Genre, Language,Users
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *

class signupForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=Users
        fields = ['usn','first_name','last_name', 'email', 'password', 'contact_no']

    def clean(self):
        cleaned_data = super(signupForm,self).clean()
        mob = cleaned_data.get("contact_no")
        if mob <1000000000 or mob >9999999999:
           raise forms.ValidationError("Invalid Mobile Number")

class loginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.widgets.PasswordInput)

    class Meta:
        model=User
        fields=['username','password']


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = feedback
        fields = [ 'rating' , 'text' ]

    def clean(self):
        cleaned_data = super(FeedbackForm,self).clean()

        rating = cleaned_data.get('rating')
        if rating > 5 and rating <1:
            raise forms.ValidationError("Invalid rating")
        text = cleaned_data.get('text')
        if text == "":
            raise forms.ValidationError("Please enter feedback")