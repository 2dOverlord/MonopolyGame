from django import forms

class SellForm(forms.Form):
    price = forms.DecimalField(label='Enter price', decimal_places=2, max_digits=5)