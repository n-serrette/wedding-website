from functools import wraps
from urllib.parse import urlparse

from django.conf import settings
from django.shortcuts import resolve_url
from django.contrib.auth import REDIRECT_FIELD_NAME

from gate.views import redirect_to_gate


def gate_lock(test_func, gate_url=None, redirect_field_name=REDIRECT_FIELD_NAME):

    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            key = request.session.get(settings.GATE_SESSION_FIELD, None)
            if test_func(key):
                return view_func(request, *args, **kwargs)
            path = request.build_absolute_uri()
            resolved_gate_url = resolve_url(gate_url or settings.GATE_URL)
            # If the gate url is the same scheme and net location then just
            # use the path as the "next" url.
            gate_scheme, gate_netloc = urlparse(resolved_gate_url)[:2]
            current_scheme, current_netloc = urlparse(path)[:2]
            if ((not gate_scheme or gate_scheme == current_scheme) and
                    (not gate_netloc or gate_netloc == current_netloc)):
                path = request.get_full_path()
            return redirect_to_gate(
                path, resolved_gate_url, redirect_field_name)

        return _wrapped_view

    return decorator
