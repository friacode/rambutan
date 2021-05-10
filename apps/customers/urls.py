from django.urls import path

from apps.customers.views import AdminCustomerListView, AdminCustomerDetailView, getOrderDetailData

app_name = 'customers'

urlpatterns = [

    path('list/', AdminCustomerListView.as_view(), name='list'),
    path('detail/<int:pk>/', AdminCustomerDetailView.as_view(), name='detail'),
    path('order-detail/', getOrderDetailData, name='order_detail'),

]
