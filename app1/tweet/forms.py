from django import forms 
from tweet.models import UserProfileInfo
from django.contrib.auth.models import User
from tweet.models import Tweet


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User 
        fields = ('username','password','email')

    
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')


class TweetModelForm(forms.ModelForm):
    content = forms.CharField(label='',
                              widget=forms.Textarea(
                                  attrs={'placeholder': 'Your message', 'class': 'form-control'})
                              )

    class Meta:
        model = Tweet
        fields = ('content',)