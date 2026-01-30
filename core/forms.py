from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Sunrise Apartments'
            }),
            'rent_type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'property_type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'rent_price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 15000'
            }),
            'deposit': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 15000'
            }),
            'area': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'sqm'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Kilimani, Nairobi'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }
