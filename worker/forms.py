from django import forms
from .models import *


class ResumeCreateForm(forms.ModelForm):

    class Meta:
        model = Resume
        fields = ['title', 'worker', 'text']


class ResumeEditForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['title', 'text']


class CompanyCreateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'workers']
