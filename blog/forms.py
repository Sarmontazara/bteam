from django import forms

from blog.models import Order


class OrderForm(forms.ModelForm):
    sale = forms.BooleanField(initial=False)
    page = forms.CharField(required=False)
    sale = forms.BooleanField(required=False)

    class Meta:
        model = Order
        fields = 'page', 'name', 'email', 'sale'
