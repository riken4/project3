from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps

def superuser_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('dashboard:login')
        if not request.user.is_superuser:
            messages.error(request, "You are not authorized to access this page.")
            return redirect('dashboard:login')
        return view_func(request, *args, **kwargs)
    return wrapper
