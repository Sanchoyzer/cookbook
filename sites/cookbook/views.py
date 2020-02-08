from django.http import HttpResponseServerError

from rest_framework.response import Response
from rest_framework.views import APIView

from .controller import CookController


class CookView(APIView):
    def get(self, request):
        try:
            result = CookController.what_can_i_cook(data=request.GET.dict())
            return Response({'data': result})
        except Exception as exc:
            return HttpResponseServerError(str(exc))
