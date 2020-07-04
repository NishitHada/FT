from django.http import JsonResponse


def success_response(key, value):
    return JsonResponse(data={
        "ok": True,
        key: value
    }, status=200)


def failure_response(message):
    return JsonResponse(data={
        "ok": False,
        "error_message": message
    }, status=400)