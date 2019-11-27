from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import SnVisibility
from .serializers import VisibilitySerializer


class VisibilityListView(APIView):
    @staticmethod
    def get(request):
        visibility = SnVisibility.objects.filter(user=request.user)
        if visibility:
            serializers = VisibilitySerializer(visibility, many=True)
            return Response(serializers.data)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def post(request):
        data = request.data
        if data:
            serializers = VisibilitySerializer(data=data)
            if serializers.is_valid():
                serializers.save()
                return Response(status.HTTP_201_CREATED)
            else:
                return Response(status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)
