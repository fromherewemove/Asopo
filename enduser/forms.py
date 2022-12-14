from django import forms

from .models import *


class ThreadForm(forms.Form):
    email = forms.CharField(label='', max_length=1000)


class MessageForm(forms.ModelForm):
    body = forms.CharField(label='', max_length=1000)
    image = forms.ImageField(required=False)

    class Meta:
        model = Message
        fields = {"body", "image"}