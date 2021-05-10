from django.urls import path

from apps.orders.views import clientOrderCreateView, clientOrderSheetView, ClientOrderListView, ClientOrderDetailView

app_name = 'orders'

urlpatterns = [

    # Client Orders
    path('list/', ClientOrderListView.as_view(), name='list'),
    path('detail/<str:code>/', ClientOrderDetailView.as_view(), name='detail'),
    path('create/', clientOrderCreateView, name='create'),
    path('sheet/<str:order_code>/', clientOrderSheetView, name='sheet'),

]
