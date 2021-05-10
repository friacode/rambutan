from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from apps.category.forms import CategoryCreationForm
from apps.category.models import Category
from apps.home.decorators import admin_account_check

has_ownership = [admin_account_check, login_required]


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AdminCategoryCreateView(CreateView):
    model = Category
    form_class = CategoryCreationForm
    template_name = 'category/create.html'

    def get_success_url(self):
        return reverse_lazy('category:list')

    def get_context_data(self, **kwargs):
        context = super(AdminCategoryCreateView, self).get_context_data(**kwargs)
        context['nav'] = "product"
        context['sub_nav'] = "category"
        return context


@method_decorator(has_ownership, 'get')
class AdminCategoryListView(ListView):
    model = Category
    template_name = 'category/list.html'
    context_object_name = 'category_list'

    def get_context_data(self, **kwargs):
        context = super(AdminCategoryListView, self).get_context_data(**kwargs)
        context['nav'] = "product"
        context['sub_nav'] = "category"
        return context


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AdminCategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryCreationForm
    context_object_name = 'target_category'
    template_name = 'category/update.html'

    def get_success_url(self):
        return reverse_lazy('category:list')

    def get_context_data(self, **kwargs):
        context = super(AdminCategoryUpdateView, self).get_context_data(**kwargs)
        context['nav'] = "product"
        context['sub_nav'] = "category"
        return context


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AdminCategoryDeleteView(DeleteView):
    model = Category
    context_object_name = 'target_category'
    success_url = reverse_lazy('category:list')
    template_name = 'category/delete.html'

    def get_context_data(self, **kwargs):
        context = super(AdminCategoryDeleteView, self).get_context_data(**kwargs)
        context['nav'] = "product"
        context['sub_nav'] = "category"
        return context
