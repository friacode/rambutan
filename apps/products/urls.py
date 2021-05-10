from django.urls import path
from apps.products.views import AdminProductListView, AdminProductDetailView, AdminProductCreateView, AdminProductUpdateView, \
    AdminProductDeleteView

app_name = 'products'

urlpatterns = [

    # Products
    path('create/', AdminProductCreateView.as_view(), name='create'),
    path('list/', AdminProductListView.as_view(), name='list'),
    path('detail/<int:pk>/', AdminProductDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', AdminProductUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', AdminProductDeleteView.as_view(), name='delete'),

]