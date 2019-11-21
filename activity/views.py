from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import SnActivity
from .serializers import ActivitySerializer


class ActivityListView(APIView):
    @staticmethod
    def get(request):
        activity = SnActivity.objects.filter(user=request.user)
        if activity:
            serializers = ActivitySerializer(activity, many=True)
            return Response(serializers.data)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def post(request):
        data = request.data
        if data:
            serializers = ActivitySerializer(data=data)
            if serializers.is_valid():
                serializers.save()
                return Response(status.HTTP_201_CREATED)
            else:
                return Response(status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)
