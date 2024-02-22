from ..models import Category
from django import forms

# Category form
class CategoryForm(forms.ModelForm):
    group = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput()
        }
