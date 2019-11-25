from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import SnAction
from .serializers import ReactSerializers
from rest_framework.response import Response


class ActionView(APIView):
    @staticmethod
    def get(request):
        react = SnAction.objects.all().filter(action_type=1)
        serializer = ReactSerializers(react, many=True)
        return Response(serializer.data)


class SearchView(APIView):
    @staticmethod
    def get(request, key):
        print("hello")
        search = User.objects.filter(username__icontains=key).values('id', 'username')
        return JsonResponse({"data": list(search)})
