from django.urls import path

from apps.default_info.views import AdminShippingTypeCreateView, AdminShippingTypeListView, AdminShippingTypeUpdateView, \
    AdminShippingTypeDeleteView, AdminPaymentTypeCreateView, AdminPaymentTypeListView, AdminPaymentTypeUpdateView, \
    AdminPaymentTypeDeleteView, AdminCurrencyTypeCreateView, AdminCurrencyTypeListView, AdminCurrencyTypeUpdateView, \
    AdminCurrencyTypeDeleteView

app_name = 'default'

urlpatterns = [

    path('shipping/create/', AdminShippingTypeCreateView.as_view(), name='shipping_create'),
    path('shipping/list/', AdminShippingTypeListView.as_view(), name='shipping_list'),
    path('shipping/update/<int:pk>', AdminShippingTypeUpdateView.as_view(), name='shipping_update'),
    path('shipping/delete/<int:pk>', AdminShippingTypeDeleteView.as_view(), name='shipping_delete'),

    path('payment/create/', AdminPaymentTypeCreateView.as_view(), name='payment_create'),
    path('payment/list/', AdminPaymentTypeListView.as_view(), name='payment_list'),
    path('payment/update/<int:pk>', AdminPaymentTypeUpdateView.as_view(), name='payment_update'),
    path('payment/delete/<int:pk>', AdminPaymentTypeDeleteView.as_view(), name='payment_delete'),

    path('currency/create/', AdminCurrencyTypeCreateView.as_view(), name='currency_create'),
    path('currency/list/', AdminCurrencyTypeListView.as_view(), name='currency_list'),
    path('currency/update/<int:pk>', AdminCurrencyTypeUpdateView.as_view(), name='currency_update'),
    path('currency/delete/<int:pk>', AdminCurrencyTypeDeleteView.as_view(), name='currency_delete'),

]