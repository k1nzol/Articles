from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from datetime import datetime

from .models import *

class AddPageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Category not selected"

    class Meta:
        model = Articles
        fields = ["title", "slug", 'publication_datetime', "content", "photo", "category"]
        widgets = {
            "content": forms.Textarea(attrs={"cols": 60, "rows": 10}),
            'publication_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local', 'required': False}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError("Length exceeds 200 characters")
        return title

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput())
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login')
    email = forms.EmailField(label='Email')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Password repeat', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CommentsForm(forms.ModelForm):
    content = forms.CharField(label="Comment", max_length=255, widget=forms.TextInput(attrs={'style': 'width: 80%;', 'placeholder': 'Comment    '}))

    class Meta:
        model = Comments
        fields = ('content',)