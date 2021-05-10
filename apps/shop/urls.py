from django.urls import path

from apps.shop.views import ClientShopListView, ClientShopDetailView

app_name = 'shop'

urlpatterns = [
    path('list/', ClientShopListView.as_view(), name='list'),
    path('detail/<int:pk>', ClientShopDetailView.as_view(), name='detail'),
]