from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, RedirectView, UpdateView, ListView, DetailView, DeleteView
from apps.address.models import Address
from apps.address.forms import AddressCreationForm


# Create your views here.
class ClientAddressListView(ListView):
    model = Address
    context_object_name = 'target_address'
    template_name = 'address/list.html'

    def get_context_data(self, **kwargs):
        context = super(ClientAddressListView, self).get_context_data(**kwargs)
        context['nav'] = 'client_address'
        return context


class ClientAddressCreateView(CreateView):
    model = Address
    form_class = AddressCreationForm
    template_name = 'address/create.html'

    def get_success_url(self):
        return reverse_lazy('address:list')

    def form_valid(self, form):
        temp_address = form.save(commit=False)
        temp_address.user = self.request.user
        temp_address.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ClientAddressCreateView, self).get_context_data(**kwargs)
        context['nav'] = 'client_address'
        return context


class ClientAddressUpdateView(UpdateView):
    model = Address
    form_class = AddressCreationForm
    context_object_name = 'target_address'
    template_name = 'address/update.html'

    def get_success_url(self):
        return reverse('address:list')

    def get_context_data(self, **kwargs):
        context = super(ClientAddressUpdateView, self).get_context_data(**kwargs)
        context['nav'] = 'client_address'
        return context


class ClientAddressDeleteView(DeleteView):
    model = Address
    context_object_name = 'target_address'
    success_url = reverse_lazy('address:list')
    template_name = 'address/delete.html'

    def get_context_data(self, **kwargs):
        context = super(ClientAddressDeleteView, self).get_context_data(**kwargs)
        context['nav'] = "client_address"
        return context
