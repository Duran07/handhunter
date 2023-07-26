from django import forms
from .models import Vacancy


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = [
            'tittle', 'salary', 'description',
            'email', 'contacts'
        ]


class VacancyEditForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = [
            'tittle', 'contacts', 'email'
        ]


