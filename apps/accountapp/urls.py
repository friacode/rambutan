from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from apps.accountapp.views import AccountCreateView, AccountUpdateView

app_name = 'accounts'

urlpatterns = [

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name='create'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),

]