from django.urls import path, include
from apps.address.views import ClientAddressListView, ClientAddressCreateView, ClientAddressUpdateView

app_name = 'address'

urlpatterns = [
    path('list/', ClientAddressListView.as_view(), name='list'),
    path('create/', ClientAddressCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ClientAddressUpdateView.as_view(), name='update'),
]