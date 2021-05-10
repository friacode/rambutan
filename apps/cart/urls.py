from django.urls import path

from apps.cart.views import CartListView, CartAddView, CartDeleteView

app_name = 'cart'

urlpatterns = [
    path('list/', CartListView.as_view(), name='list'),
    path('add/', CartAddView.as_view(), name='add'),
    path('delete/', CartDeleteView.as_view(), name='delete'),
]