from functools import wraps
from django.http import HttpResponseRedirect




def auth_only(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect("/login")
    return wrapper

