from ..forms import SearchForm
from ..models import Expense
from django import forms

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'date', 'description', 'amount']
        widgets = {
            'category': forms.Select(),
            'date': forms.TextInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
            'amount': forms.NumberInput(attrs={'step': '0.01'})
        }
        
class ExpenseSearchForm(SearchForm):
    expense_id = forms.IntegerField(required=False)
    