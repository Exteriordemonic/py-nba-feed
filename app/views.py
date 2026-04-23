from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView


def health(request):
    return HttpResponse("ok", content_type="text/plain")


class ApiHealthView(APIView):
    def get(self, request):
        return Response({"status": "ok"})
