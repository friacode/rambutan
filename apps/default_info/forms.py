from django.forms import ModelForm

from apps.default_info.models import ShippingType, PaymentType, CurrencyType


class ShippingTypeCreationForm(ModelForm):

    class Meta:
        model = ShippingType
        fields = ['name', 'fee', 'status']


class PaymentTypeCreationForm(ModelForm):

    class Meta:
        model = PaymentType
        fields = ['name']


class CurrencyTypeCreationForm(ModelForm):

    class Meta:
        model = CurrencyType
        fields = ['code', 'name', 'unit', 'status']
