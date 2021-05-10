from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms


class AccountUpdateForm(ModelForm):
    phone = forms.CharField(label='연락처', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone']

