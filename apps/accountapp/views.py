from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from apps.accountapp.forms import AccountUpdateForm
from apps.coreapp.views import getCategory
from apps.customers.models import Customer


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accounts:login')
    template_name = 'accountapp/create.html'

    def get_context_data(self, **kwargs):
        context = super(AccountCreateView, self).get_context_data(**kwargs)
        context['category'] = getCategory()
        return context

    def form_valid(self, form):
        temp_user = form.save(commit=False)
        temp_user.save()
        Customer(user=temp_user, status=True).save()
        return super().form_valid(form)


class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    template_name = 'accountapp/update.html'

    def get_success_url(self):
        return reverse('accounts:update', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = getCategory()
        context['nav'] = 'client_account'
        customer = Customer.objects.get(user=self.object)
        context['phone'] = customer.phone

        return context

    def form_valid(self, form):
        temp_user = form.save(commit=False)
        customer = Customer.objects.get(user=temp_user)
        customer.phone = self.request.POST['phone']
        customer.save()
        temp_user.save()

        return super().form_valid(form)


