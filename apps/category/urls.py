from django.urls import path

from apps.category.views import AdminCategoryCreateView, AdminCategoryListView, AdminCategoryUpdateView, AdminCategoryDeleteView

app_name = 'category'

urlpatterns = [
    path('create/', AdminCategoryCreateView.as_view(), name='create'),
    path('list/', AdminCategoryListView.as_view(), name='list'),
    path('update/<int:pk>', AdminCategoryUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AdminCategoryDeleteView.as_view(), name='delete'),
]