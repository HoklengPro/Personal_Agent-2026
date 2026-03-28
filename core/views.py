from django.http import JsonResponse


def health(request):
    return JsonResponse({"status": "ok", "message": "Django is running!"})


def index(request):
    return JsonResponse({"app": "My Django Project", "version": "1.0.0"})
