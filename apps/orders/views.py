from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView, RedirectView, UpdateView, ListView, DetailView

from apps.cart.models import Cart
from apps.orders.models import Order, OrderDetail
from apps.coreapp.views import getCategory
from apps.default_info.models import CurrencyType

import string
import random
LENGTH = 8


def clientOrderCreateView(request):
    context = {}
    cart = Cart.objects.filter(user=request.user)
    string_pool = string.ascii_uppercase + string.digits
    code = ''
    for item in range(LENGTH):
        code += random.choice(string_pool)
    order = Order(user=request.user, code=code, status='CREATE')
    order.save()

    sale_price = 0

    for item in cart:

        if item.product.saleOption == 'FA':
            sale_price = item.product.price - item.product.salePrice
        elif item.product.saleOption == 'DR':
            sale_ratio = item.product.price * (item.product.salePrice * 0.01)
            sale_price = int(item.product.price - sale_ratio)

        total_price = item.product.price - sale_price + 2500

        order_detail = OrderDetail(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price * item.quantity,
            sale_price=sale_price * item.quantity,
            shipping_fee=2500,
            total_price=total_price * item.quantity
        )
        order_detail.save()

        # cart status change
        item.status = False
        item.save()
        context['order_code'] = code
        context['category'] = getCategory()

    return HttpResponseRedirect(reverse('orders:sheet', kwargs={'order_code': code}))


def clientOrderSheetView(request, order_code):
    context = {}
    order = Order.objects.get(code=order_code, user=request.user)
    context['order'] = order
    order_detail = OrderDetail.objects.filter(order=order)
    context['order_detail'] = order_detail
    context['category'] = getCategory()
    return render(request, 'orders/create.html', context)


class ClientOrderListView(ListView):
    model = Order
    context_object_name = 'target_orders'
    template_name = 'orders/list.html'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = getCategory()
        context['nav'] = 'client_orders'
        return context


class ClientOrderDetailView(ListView):
    model = OrderDetail
    template_name = 'orders/detail.html'
    context_object_name = 'target_order_detail'

    def get_queryset(self):
        order = Order.objects.get(code=self.kwargs['code'])
        return OrderDetail.objects.filter(order=order)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ClientOrderDetailView, self).get_context_data(**kwargs)
        order = Order.objects.get(code=self.kwargs['code'])
        context['order'] = order
        context['nav'] = 'client_orders'

        # Currency info
        currency = CurrencyType.objects.get(status=True)
        context['currency'] = currency.name

        order_detail = OrderDetail.objects.filter(order=order)
        price = 0
        shipping_fee = 0
        sale_price = 0
        total_price = 0

        for item in order_detail:
            price = price + item.price
            sale_price = sale_price + item.sale_price
            total_price = total_price + item.total_price
            shipping_fee = item.shipping_fee

        context['price'] = price
        context['sale_price'] = sale_price
        context['shipping_fee'] = shipping_fee
        context['total_price'] = total_price

        context['category'] = getCategory()

        return context
