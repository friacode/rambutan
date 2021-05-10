from django.urls import path

from apps.brand.views import AdminBrandCreateView, AdminBrandListView, AdminBrandUpdateView, AdminBrandDeleteView

app_name = 'brand'

urlpatterns = [
    path('create/', AdminBrandCreateView.as_view(), name='create'),
    path('list/', AdminBrandListView.as_view(), name='list'),
    path('update/<int:pk>', AdminBrandUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AdminBrandDeleteView.as_view(), name='delete'),
]