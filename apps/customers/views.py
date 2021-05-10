from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from apps.cart.models import Cart
from apps.customers.models import Customer
from apps.orders.models import OrderDetail, Order
from apps.wishlist.models import Wishlist


class AdminCustomerListView(ListView):
    model = Customer
    context_object_name = 'customers_list'
    template_name = 'customers/list.html'

    def get_context_data(self, **kwargs):
        context = super(AdminCustomerListView, self).get_context_data(**kwargs)
        context['nav'] = "customer"
        return context


class AdminCustomerDetailView(DetailView):
    model = Customer
    context_object_name = 'target_customer'
    template_name = 'customers/detail.html'

    def get_context_data(self, **kwargs):
        context = super(AdminCustomerDetailView, self).get_context_data(**kwargs)
        context['nav'] = "customer"

        # Wish list
        wishlist = Wishlist.objects.filter(user=self.object.user)
        context['wishlist'] = wishlist

        # Cart list
        cart = Cart.objects.filter(user=self.object.user)
        context['cart'] = cart

        # Order list
        order = Order.objects.filter(user=self.object.user)
        context['order'] = order

        return context


def getOrderDetailData(request):
    context = {}
    context['nav'] = "customer"
    order_code = request.GET['order_code']
    order = Order.objects.get(code=order_code)
    order_detail = OrderDetail.objects.filter(order=order)
    context['order_detail'] = order_detail

    return render(request, 'customers/order_detail.html', context)
