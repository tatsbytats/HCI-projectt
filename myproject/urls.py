"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from boards import views
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse
import os

def debug_static(request):
    """Temporary view to diagnose static files"""
    if not settings.DEBUG and not settings.ALLOWED_HOSTS == ['*']:
        return JsonResponse({"error": "Unauthorized"}, status=403)
    
    def list_files(directory):
        results = []
        if os.path.exists(directory):
            for root, _, files in os.walk(directory):
                for f in files:
                    full_path = os.path.join(root, f)
                    rel_path = os.path.relpath(full_path, directory)
                    results.append(rel_path)
        return results

    return JsonResponse({
        "STATIC_ROOT": str(settings.STATIC_ROOT),
        "STATIC_URL": settings.STATIC_URL,
        "STATICFILES_DIRS": [str(d) for d in getattr(settings, 'STATICFILES_DIRS', [])],
        "static_root_files": list_files(str(settings.STATIC_ROOT)) if hasattr(settings, 'STATIC_ROOT') else [],
        "debug": settings.DEBUG,
        "using_whitenoise": any("whitenoise" in m.lower() for m in settings.MIDDLEWARE)
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('boards.urls')),  # includes the boards app URLs
    path('__debug_static/', debug_static),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






