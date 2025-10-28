from django.http import JsonResponse
import os
from django.conf import settings

def list_static_files(request):
    """Temporary debug view to list collected static files"""
    if not settings.DEBUG:
        return JsonResponse({"error": "Debug only"}, status=403)
    
    static_files = []
    static_root = settings.STATIC_ROOT
    static_dirs = settings.STATICFILES_DIRS
    
    # List files in STATIC_ROOT
    if os.path.exists(static_root):
        for root, dirs, files in os.walk(static_root):
            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, static_root)
                static_files.append({
                    "path": rel_path,
                    "source": "STATIC_ROOT",
                    "exists": True
                })
    
    # List files in STATICFILES_DIRS
    for static_dir in static_dirs:
        if os.path.exists(static_dir):
            for root, dirs, files in os.walk(static_dir):
                for file in files:
                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, static_dir)
                    static_files.append({
                        "path": rel_path,
                        "source": "STATICFILES_DIRS",
                        "exists": True
                    })
    
    return JsonResponse({
        "static_root": static_root,
        "static_dirs": static_dirs,
        "files": static_files
    })