from ..models import Category, CATEGORY_CHOICES
from django import forms

class CategoryForm(forms.ModelForm):
    group = forms.ChoiceField(label='Category Group', choices=CATEGORY_CHOICES.items(), widget=forms.Select(attrs={'class':'form-control'}))
    name = forms.CharField(label='Category Name', max_length=60, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Category Name'}))

    class Meta:
        model = Category
        fields = ['group', 'name']
