class SetRemoteAddrFromForwardedFor:
    """Middleware that replaces REMOTE_ADDR with the first value from
    X-Forwarded-For if present. This is appropriate when your app is
    behind a trusted proxy (for example Render). Use with caution and
    only when you control the proxy.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        xff = request.META.get('HTTP_X_FORWARDED_FOR')
        if xff:
            # X-Forwarded-For can contain a comma-separated list. The
            # client's IP is the first in the list.
            try:
                client_ip = xff.split(',')[0].strip()
                if client_ip:
                    request.META['REMOTE_ADDR'] = client_ip
            except Exception:
                # Be defensive: if parsing fails, leave REMOTE_ADDR as-is.
                pass
        return self.get_response(request)
