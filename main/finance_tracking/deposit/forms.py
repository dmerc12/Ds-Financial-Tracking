from ..models import Deposit, Category
from ..forms import SearchForm
from django import forms

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
        
class DepositSearchForm(SearchForm):
    deposit_id = forms.IntegerField(required=False)
    category = forms.ModelChoiceField(
        queryset=Category.objects.filter(group='deposit'),
        required=False,
        empty_label="All Deposit Categories"
    )

    def __init__(self, user, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(user=user, group='deposit')
