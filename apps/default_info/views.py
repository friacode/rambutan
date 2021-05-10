from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from apps.default_info.forms import ShippingTypeCreationForm, PaymentTypeCreationForm, CurrencyTypeCreationForm
from apps.default_info.models import ShippingType, PaymentType, CurrencyType
from apps.home.decorators import admin_account_check

has_ownership = [admin_account_check, login_required]


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AdminShippingTypeCreateView(CreateView):
    model = ShippingType
    form_class = ShippingTypeCreationForm
    template_name = 'default_info/shipping_type/create.html'

    def get_success_url(self):
        return reverse_lazy('default:shipping_list')

    def get_context_data(self, **kwargs):
        context = super(AdminShippingTypeCreateView, self).get_context_data(**kwargs)
        context['nav'] = "default"
        context['sub_nav'] = "ship"
        return context


@method_decorator(has_ownership, 'get')
class AdminShippingTypeListView(ListView):
    model = ShippingType
    template_name = 'default_info/shipping_type/list.html'
    context_object_name = 'shipping_list'

    def get_context_data(self, **kwargs):
        context = super(AdminShippingTypeListView, self).get_context_data(**kwargs)
        context['nav'] = "default"
        context['sub_nav'] = "ship"
        return context


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AdminShippingTypeUpdateView(UpdateView):
    model = ShippingType
    form_class = ShippingTypeCreationForm
    context_object_name = 'target_shipping'
    template_name = 'default_info/shipping_type/update.html'

    def get_success_url(self):
        return reverse_lazy('default:shipping_list')

    def get_context_data(self, **kwargs):
        context = super(AdminShippingTypeUpdateView, self).get_context_data(**kwargs)
        context['nav'] = "default"
        context['sub_nav'] = "ship"
        return context


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AdminShippingTypeDeleteView(DeleteView):
    model = ShippingType
    context_object_name = 'target_shipping'
    success_url = reverse_lazy('default:shipping_list')
    template_name = 'default_info/shipping_type/delete.html'

    def get_context_data(self, **kwargs):
        context = super(AdminShippingTypeDeleteView, self).get_context_data(**kwargs)
        context['nav'] = "default"
        context['sub_nav'] = "ship"
        return context


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AdminPaymentTypeCreateView(CreateView):
    model = PaymentType
    form_class = PaymentTypeCreationForm
    template_name = 'default_info/payment_type/create.html'

    def get_success_url(self):
        return reverse_lazy('default:payment_list')

    def get_context_data(self, **kwargs):
        context = super(AdminPaymentTypeCreateView, self).get_context_data(**kwargs)
        context['nav'] = "default"
        context['sub_nav'] = "payment"
        return context


@method_decorator(has_ownership, 'get')
class AdminPaymentTypeListView(ListView):
    model = PaymentType
    template_name = 'default_info/payment_type/list.html'
    context_object_name = 'payment_list'

    def get_context_data(self, **kwargs):
        context = super(AdminPaymentTypeListView, self).get_context_data(**kwargs)
        context['nav'] = "default"
        context['sub_nav'] = "payment"
        return context


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AdminPaymentTypeUpdateView(UpdateView):
    model = PaymentType
    form_class = PaymentTypeCreationForm
    context_object_name = 'target_payment'
    template_name = 'default_info/payment_type/update.html'

    def get_success_url(self):
        return reverse_lazy('default:payment_list')

    def get_context_data(self, **kwargs):
        context = super(AdminPaymentTypeUpdateView, self).get_context_data(**kwargs)
        context['nav'] = "default"
        context['sub_nav'] = "payment"
        return context


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AdminPaymentTypeDeleteView(DeleteView):
    model = PaymentType
    context_object_name = 'target_payment'
    success_url = reverse_lazy('default:payment_list')
    template_name = 'default_info/payment_type/delete.html'

    def get_context_data(self, **kwargs):
        context = super(AdminPaymentTypeDeleteView, self).get_context_data(**kwargs)
        context['nav'] = "default"
        context['sub_nav'] = "payment"
        return context


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AdminCurrencyTypeCreateView(CreateView):
    model = CurrencyType
    form_class = CurrencyTypeCreationForm
    template_name = 'default_info/currency_type/create.html'

    def get_success_url(self):
        return reverse_lazy('default:currency_list')

    def get_context_data(self, **kwargs):
        context = super(AdminCurrencyTypeCreateView, self).get_context_data(**kwargs)
        context['nav'] = "default"
        context['sub_nav'] = "currency"
        return context


@method_decorator(has_ownership, 'get')
class AdminCurrencyTypeListView(ListView):
    model = CurrencyType
    template_name = 'default_info/currency_type/list.html'
    context_object_name = 'currency_list'

    def get_context_data(self, **kwargs):
        context = super(AdminCurrencyTypeListView, self).get_context_data(**kwargs)
        context['nav'] = "default"
        context['sub_nav'] = "currency"
        return context


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AdminCurrencyTypeUpdateView(UpdateView):
    model = CurrencyType
    form_class = CurrencyTypeCreationForm
    context_object_name = 'target_currency'
    template_name = 'default_info/currency_type/update.html'

    def get_success_url(self):
        return reverse_lazy('default:currency_list')

    def get_context_data(self, **kwargs):
        context = super(AdminCurrencyTypeUpdateView, self).get_context_data(**kwargs)
        context['nav'] = "default"
        context['sub_nav'] = "currency"
        return context


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AdminCurrencyTypeDeleteView(DeleteView):
    model = CurrencyType
    context_object_name = 'target_currency'
    success_url = reverse_lazy('default:currency_list')
    template_name = 'default_info/currency_type/delete.html'

    def get_context_data(self, **kwargs):
        context = super(AdminCurrencyTypeDeleteView, self).get_context_data(**kwargs)
        context['nav'] = "default"
        context['sub_nav'] = "currency"
        return context
