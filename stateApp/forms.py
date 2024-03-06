from django import forms
from .models import State

class StateModelForm(forms.ModelForm):
    class Meta:
        model = State
        fields = ['name', 'population','language','capital']