from django.urls import path, include

urlpatterns = [

    # Index Page
    path('', include('apps.home.urls')),

    # Account App
    path('accounts/', include('apps.accountapp.urls')),

    # Address
    path('address/', include('apps.address.urls')),

    # Shop
    path('shop/', include('apps.shop.urls')),

    # Cart
    path('cart/', include('apps.cart.urls')),

    # Wishlist
    path('wishlist/', include('apps.wishlist.urls')),

    # Orders
    path('orders/', include('apps.orders.urls')),

    # Admin Products
    path('administrator/products/', include('apps.products.urls')),

    # Admin Category
    path('administrator/category/', include('apps.category.urls')),

    # Admin Brand
    path('administrator/brand/', include('apps.brand.urls')),

    # Admin Default Information
    path('administrator/default/', include('apps.default_info.urls')),

    # Admin Customers
    path('administrator/customers/', include('apps.customers.urls')),

    # Admin Manage Order
    path('administrator/orders/', include('apps.manage_order.urls')),

]
