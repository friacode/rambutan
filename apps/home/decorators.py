from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def admin_account_check(func):
    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=request.user.pk)
        if not user.is_staff:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated
