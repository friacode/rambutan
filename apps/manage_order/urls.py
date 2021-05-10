from django.urls import path

from apps.manage_order.views import AdminManageOrderListView, AdminManageOrderDetailView

app_name = 'manage_order'

urlpatterns = [

    path('list/', AdminManageOrderListView.as_view(), name='list'),
    path('detail/<str:code>/', AdminManageOrderDetailView.as_view(), name='detail'),

]