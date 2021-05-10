from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, RedirectView

from apps.cart.models import Cart
from apps.products.models import Product
from apps.coreapp.views import getCategory, getCurrency


class CartListView(ListView):
    model = Cart
    # context_object_name = 'target_cart'
    template_name = 'cart/list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        carts = Cart.objects.filter(user=self.request.user)
        context['carts'] = carts

        sale_price = 0
        org_price = 0
        discount_price = 0

        for item in carts:
            org_price = org_price + (item.quantity * item.product.price)
            if item.product.saleOption == 'FA':
                sale_price = sale_price + (item.quantity * (item.product.price - item.product.salePrice))
                discount_price = discount_price + (item.quantity * item.product.salePrice)
            elif item.product.saleOption == 'DR':
                sale_percent = item.product.price * (item.product.salePrice * 0.01)
                sale_price = sale_price + (item.quantity * item.product.price - int(sale_percent))
                discount_price = discount_price + (item.quantity * int(sale_percent))
            else:
                sale_price = sale_price + (item.quantity * item.product.price)

        context['sale_price'] = sale_price
        context['org_price'] = org_price
        context['discount_price'] = discount_price
        context['category'] = getCategory()
        context['currency'] = getCurrency()

        return context


class CartAddView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('shop:detail', kwargs={'pk': self.request.GET.get('product_pk')})

    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=self.request.GET.get('product_pk'))
        user = self.request.user
        cart = Cart.objects.filter(user=user, product=product)
        if cart.exists():
            cart.delete()
        else:
            Cart(product=product, user=user, quantity=self.request.GET.get('quantity')).save()
        return super(CartAddView, self).get(request, *args, **kwargs)


class CartDeleteView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('cart:list')

    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=self.request.GET.get('product_pk'))
        user = self.request.user
        cart = Cart.objects.filter(user=user, product=product)
        if cart.exists():
            cart.delete()
        return super(CartDeleteView, self).get(request, *args, **kwargs)
