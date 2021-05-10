from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from apps.orders.models import Order, OrderDetail


class AdminManageOrderListView(ListView):
    model = Order
    context_object_name = 'order_list'
    template_name = 'manage_orders/list.html'

    def get_context_data(self, **kwargs):
        context = super(AdminManageOrderListView, self).get_context_data(**kwargs)
        context['nav'] = "order"
        return context


class AdminManageOrderDetailView(ListView):
    model = OrderDetail
    template_name = 'manage_orders/detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AdminManageOrderDetailView, self).get_context_data(**kwargs)
        context['nav'] = "order"

        order = Order.objects.get(code=self.kwargs['code'])
        context['order'] = order

        order_detail = OrderDetail.objects.filter(order=order)
        context['order_detail'] = order_detail

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
        return context

