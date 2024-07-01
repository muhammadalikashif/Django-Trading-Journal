from django import forms
from .models import Trade

class TradeForm(forms.ModelForm):
    class Meta:
        model = Trade
        fields = '__all__'
        exclude = ('result', 'profit_loss', 'user')  # Exclude 'user' field as an example
        
    # Use widgets to apply form-control class
    position = forms.ChoiceField(
        choices=Trade.POSITION_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    entry_price = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    
    exit_price = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    # Add widget definitions for other fields
    symbol = forms.CharField(
    widget=forms.TextInput(attrs={'class': 'form-control'})
)
    observations = forms.CharField(
    widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
)

    setup_image = forms.ImageField(
    widget=forms.FileInput(attrs={'class': 'form-control'})
)

    reasons_for_entry = forms.CharField(
    widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
)

