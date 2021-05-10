from django.forms import ModelForm

from apps.address.models import Address


class AddressCreationForm(ModelForm):

    class Meta:
        model = Address
        fields = ['baseDelivery', 'title', 'name', 'postcode', 'addr', 'addr_detail']
