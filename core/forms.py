from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            'name', 'rent_type', 'property_type',
            'rent_price', 'deposit', 'area',
            'location', 'description', 'image'
        ]

        widgets = {
            'rent_type': forms.Select(attrs={'class': 'form-control'}),
            'property_type': forms.Select(attrs={'class': 'form-control'}),
        }
