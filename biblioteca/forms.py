# biblioteca/forms.py
from django import forms
from .models import Llibre

class LlibreForm(forms.ModelForm):
    class Meta:
        model = Llibre
        fields = ['titol', 'autor', 'ISBN', 'editorial', 'colleccio', 'llengua', 'pais', 'pagines']