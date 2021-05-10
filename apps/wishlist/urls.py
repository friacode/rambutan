from django.urls import path

from apps.wishlist.views import WishlistAddView, WishlistListView

app_name = 'wishlist'

urlpatterns = [
    path('add/', WishlistAddView.as_view(), name='add'),
    path('list/', WishlistListView.as_view(), name='list'),

]

