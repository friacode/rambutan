from django.forms import ModelForm

from apps.orders.models import Order, OrderDetail


class ClientOrderCreationForm(ModelForm):
    class Meta:
        model = OrderDetail
        fields = ['request_text']