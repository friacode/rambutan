from django.urls import path

from apps.home.views import clientIndexPage, administratorIndexPage, AdminLoginView, AdminLogoutView, updateSuperUser

app_name = 'home'

urlpatterns = [

    # Client Index Page
    path('', clientIndexPage, name='client_index_page'),

    # Administrator Index Page
    path('administrator/', administratorIndexPage, name='administrator_index_page'),

    # Administrator Login
    path('administrator/login/', AdminLoginView.as_view(), name='admin_login'),
    path('administrator/logout/', AdminLogoutView.as_view(), name='admin_logout'),

    # update superuser
    # path('administrator/update-user/', updateSuperUser, name='update-user')

]
