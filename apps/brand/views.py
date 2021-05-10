from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from apps.brand.forms import BrandCreationForm
from apps.brand.models import Brand
from apps.home.decorators import admin_account_check

has_ownership = [admin_account_check, login_required]


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AdminBrandCreateView(CreateView):
    model = Brand
    form_class = BrandCreationForm
    template_name = 'brand/create.html'

    def get_success_url(self):
        return reverse_lazy('brand:list')

    def get_context_data(self, **kwargs):
        context = super(AdminBrandCreateView, self).get_context_data(**kwargs)
        context['nav'] = "product"
        context['sub_nav'] = "brand"
        return context


@method_decorator(has_ownership, 'get')
class AdminBrandListView(ListView):
    model = Brand
    template_name = 'brand/list.html'
    context_object_name = 'brand_list'

    def get_context_data(self, **kwargs):
        context = super(AdminBrandListView, self).get_context_data(**kwargs)
        context['nav'] = "product"
        context['sub_nav'] = "brand"
        return context


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AdminBrandUpdateView(UpdateView):
    model = Brand
    form_class = BrandCreationForm
    context_object_name = 'target_brand'
    template_name = 'brand/update.html'

    def get_success_url(self):
        return reverse_lazy('brand:list')

    def get_context_data(self, **kwargs):
        context = super(AdminBrandUpdateView, self).get_context_data(**kwargs)
        context['nav'] = "product"
        context['sub_nav'] = "brand"
        return context


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AdminBrandDeleteView(DeleteView):
    model = Brand
    context_object_name = 'target_brand'
    success_url = reverse_lazy('brand:list')
    template_name = 'brand/delete.html'

    def get_context_data(self, **kwargs):
        context = super(AdminBrandDeleteView, self).get_context_data(**kwargs)
        context['nav'] = "product"
        context['sub_nav'] = "brand"
        return context
