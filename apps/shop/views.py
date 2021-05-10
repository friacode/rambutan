from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from apps.cart.models import Cart
from apps.category.models import Category
from apps.products.models import Product
from apps.wishlist.models import Wishlist
from apps.coreapp.views import getCategory, getCurrency


class ClientShopListView(ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'shop/list.html'

    def get_queryset(self):
        if self.request.GET.get('category'):
            category = self.request.GET['category']
            category_object = Category.objects.get(name=category)
            product = Product.objects.filter(category=category_object)
        else:
            product = Product.objects.all()

        return product

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET.get('category'):
            context['category_name'] = self.request.GET['category']
        context['category'] = getCategory()
        context['currency'] = getCurrency()

        return context


class ClientShopDetailView(DetailView):
    model = Product
    context_object_name = 'target_product'
    template_name = 'shop/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.object
        if product.saleOption == 'FA':
            context['salePrice'] = product.price - product.salePrice
        elif product.saleOption == 'DR':
            salePrice = product.price * (product.salePrice * 0.01)
            context['salePrice'] = int(product.price - salePrice)

        if self.request.user.is_authenticated:
            cart = Cart.objects.filter(user=self.request.user, product=product)
            if cart.exists():
                context['cart'] = '1'
            else:
                context['cart'] = '0'

            wishlist = Wishlist.objects.filter(user=self.request.user, product=product)
            if wishlist.exists():
                context['wishlist'] = '1'
            else:
                context['wishlist'] = '0'
        else:
            context['cart'] = '0'
            context['wishlist'] = '0'

        context['category'] = getCategory()
        context['currency'] = getCurrency()

        return context

