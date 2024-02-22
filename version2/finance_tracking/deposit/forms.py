from ..models import Deposit, Category
from ..forms import SearchForm
from django import forms

# Deposit form
class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = ['category', 'date', 'description', 'amount']
        widgets = {
            'category': forms.Select(),
            'date': forms.TextInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
            'amount': forms.NumberInput(attrs={'step': '0.01'})
        }

# Deposit search form    
class DepositSearchForm(SearchForm):
    deposit_id = forms.IntegerField(required=False)
