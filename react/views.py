from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, status
from .models import SnReactPost, SnReactShare
from .serializers import ReactPostSerializers, ShareSerializers
from rest_framework.response import Response


class PostReactApiList(APIView):
    @staticmethod
    def get(request, pk):
        data = SnReactPost.objects.filter(user=request.user.id, post=pk)
        serializer = ReactPostSerializers(data, many=True)
        print("Data is ", data)
        if data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @staticmethod
    def post(request, pk):
        form_data = request.data
        data = {"user": request.user.id, "post": pk,
                "react_type": form_data["react_type"]}
        serializers = ReactPostSerializers(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response({"status": "Success"}, status.HTTP_201_CREATED)
        else:
            return Response({"status": serializers.errors}, status.HTTP_406_NOT_ACCEPTABLE)

    @staticmethod
    def patch(request, pk):
        form_data = request.data
        data = {"user": request.user.id, "post": pk,
                "react_type": form_data["react_type"]}
        react = get_object_or_404(SnReactPost, pk=pk)
        serializers = ReactPostSerializers(react, data=data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response({"status": "Success"}, status.HTTP_201_CREATED)
        else:
            return Response({"status": serializers.errors}, status.HTTP_406_NOT_ACCEPTABLE)


class ShareReactApiList(APIView):
    @staticmethod
    def get(request, pk):
        reacts = SnReactShare.objects.all().filter(share=pk)
        if reacts:
            serializers = ShareSerializers(SnReactShare, many=True)
            return Response(serializers.data)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)
