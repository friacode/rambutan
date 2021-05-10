from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.views.generic import RedirectView, ListView

from apps.products.models import Product
from apps.wishlist.models import Wishlist
from apps.coreapp.views import getCategory, getCurrency


class WishlistListView(ListView):
    model = Wishlist
    context_object_name = 'target_wishlist'
    template_name = 'wishlist/list.html'

    def get_queryset(self):
        target_wishlist = Wishlist.objects.filter(user=self.request.user)
        return target_wishlist

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WishlistListView, self).get_context_data()
        context['category'] = getCategory()
        context['currency'] = getCurrency()
        context['nav'] = 'client_wish'
        return context


class WishlistAddView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('shop:detail', kwargs={'pk': self.request.GET.get('product_pk')})

    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=self.request.GET.get('product_pk'))
        user = self.request.user
        wishlist = Wishlist.objects.filter(user=user, product=product)
        if wishlist.exists():
            wishlist.delete()
        else:
            Wishlist(product=product, user=user).save()
        return super(WishlistAddView, self).get(request, *args, **kwargs)
