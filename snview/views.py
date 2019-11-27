from rest_framework.views import APIView,status
from rest_framework.response import Response
from .models import SnPostView, SnShareView
from .serializers import PostViewSerializers, ShareViewSerializers


class PostVisitView(APIView):
    @staticmethod
    def get(request, pk):
        __view = SnPostView.objects.filter(post=pk)
        print(__view)
        if __view:
            serializers = PostViewSerializers(__view, many=True)
            return Response(serializers.data)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def post(request, pk):
        data = request.data
        serializers = PostViewSerializers(data=data)
        if serializers.is_valid():
            serializers.save()
        else:
            return Response({"response": "Save Error"}, status=status.HTTP_400_BAD_REQUEST)


class ShareVisitView(APIView):
    @staticmethod
    def get(request, pk):
        view = SnShareView.objects.all()
        serializers = ShareViewSerializers(view, many=True)
        return Response(serializers.data)

    @staticmethod
    def post(request, pk):
        data = request.data
        serializers = ShareViewSerializers(data=data)
        if serializers.is_valid():
            serializers.save()
        else:
            return Response({"response": "Save Error"}, status=status.HTTP_400_BAD_REQUEST)


