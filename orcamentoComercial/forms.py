from django import forms
from .models import OrcamentoComercial

class OrcamentoComercialForm(forms.ModelForm):
    margem = forms.DecimalField(widget=forms.NumberInput(attrs={'type': 'range', 'min': '0', 'max': '100', 'step': '0.1'}))

    class Meta:
        model = OrcamentoComercial
        fields = '__all__'
