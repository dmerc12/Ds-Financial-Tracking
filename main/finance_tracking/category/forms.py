from django import forms

from ..models import Category

class CategoryForm(forms.ModelForm):
    group = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput()
        }
