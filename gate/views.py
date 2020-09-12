from urllib.parse import urlparse, urlunparse
from django.conf import settings

from django.http import HttpResponseRedirect, QueryDict
from django.shortcuts import resolve_url

from gate import REDIRECT_FIELD_NAME


def redirect_to_gate(next, gate_url=None, redirect_field_name=REDIRECT_FIELD_NAME):
    """
    Redirect the user to the gate page, passing the given 'next' page.
    """
    resolved_url = resolve_url(gate_url or settings.GATE_URL)

    gate_url_parts = list(urlparse(resolved_url))
    if redirect_field_name:
        querystring = QueryDict(gate_url_parts[4], mutable=True)
        querystring[redirect_field_name] = next
        gate_url_parts[4] = querystring.urlencode(safe='/')

    return HttpResponseRedirect(urlunparse(gate_url_parts))


def set_key(request, key):
    request.session[settings.GATE_SESSION_FIELD] = key
