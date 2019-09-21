from django import forms
from django.forms import widgets
from webapp.models import PRODUCT_CATEGORY_CHOICES


class ProductForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Название')
    description = forms.CharField(max_length=2000, required=True, label='Описание',widget=widgets.Textarea)
    category = forms.ChoiceField(label='Категория', choices=PRODUCT_CATEGORY_CHOICES)
    amount = forms.IntegerField(label='Остаток', required=True)
    price = forms.IntegerField(label='Цена', required=True)
