from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from apps.coreapp.views import getCurrency
from apps.products.models import Product, ProductImage
from apps.products.forms import ProductCreationForm
from apps.home.decorators import admin_account_check
from apps.coreapp.views import rescale

import string
import random
LENGTH = 8

has_ownership = [admin_account_check, login_required]


# Create your views here.
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AdminProductCreateView(CreateView):
    model = Product
    form_class = ProductCreationForm
    template_name = 'products/create.html'

    def form_valid(self, form):
        temp_product = form.save(commit=False)
        string_pool = string.ascii_uppercase + string.digits
        result = ''

        for item in self.request.FILES.getlist('product_img_file'):
            product_image = ProductImage(product=product, image=item)
            product_image.save()

        for item in range(LENGTH):
            result += random.choice(string_pool)
        temp_product.code = result
        temp_product.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(AdminProductCreateView, self).get_context_data(**kwargs)
        context['nav'] = "product"
        context['sub_nav'] = "list"
        return context

    def get_success_url(self):
        return reverse('products:detail', kwargs={'pk': self.object.pk})


@method_decorator(has_ownership, 'get')
class AdminProductListView(ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'products/list.html'

    def get_context_data(self, **kwargs):
        context = super(AdminProductListView, self).get_context_data(**kwargs)
        context['nav'] = "product"
        context['sub_nav'] = "list"
        return context


@method_decorator(has_ownership, 'get')
class AdminProductDetailView(DetailView):
    model = Product
    form_class = ProductCreationForm
    context_object_name = 'target_product'
    template_name = 'products/detail.html'

    def get_context_data(self, **kwargs):
        context = super(AdminProductDetailView, self).get_context_data(**kwargs)
        context['nav'] = 'product'
        context['sub_nav'] = 'list'
        context['currency'] = getCurrency()
        return context


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AdminProductUpdateView(UpdateView):
    model = Product
    form_class = ProductCreationForm
    context_object_name = 'target_product'
    template_name = 'products/update.html'
    
    def get_success_url(self):
        return reverse('products:detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(AdminProductUpdateView, self).get_context_data(**kwargs)
        context['nav'] = "product"
        context['sub_nav'] = "list"
        return context

    def form_valid(self, form):
        temp_product = form.save(commit=False)
        product = Product.objects.get(pk=temp_product.pk)

        for item in self.request.FILES.getlist('product_img_file'):
            product_image = ProductImage(product=product, image=item)
            product_image.save()

        temp_product.save()
        return super().form_valid(form)


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AdminProductDeleteView(DeleteView):
    model = Product
    context_object_name = 'target_product'
    success_url = reverse_lazy('products:list')
    template_name = 'products/delete.html'

    def get_context_data(self, **kwargs):
        context = super(AdminProductDeleteView, self).get_context_data(**kwargs)
        context['nav'] = "product"
        context['sub_nav'] = "list"
        return context


