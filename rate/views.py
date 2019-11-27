from rest_framework.views import APIView, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import (
    SnRateShare, SnRateShareReplay, SnRatePostReplay,
    SnRateShareComment, SnRatePostComment, SnRatePost
)
from .serializers import RatePostSerializers, RateShareSerializers,\
    RatePostCommentSerializers, RatePostReplaySerializers, RateShareCommentSerializers,\
    RateShareReplaySerializers
# Create your views here.


class RatePostView(APIView):

    @staticmethod
    def get(request, pk):
        rate = get_object_or_404(SnRatePost, pk=pk)
        if rate:
            serializers = RatePostSerializers(rate)
            return Response(serializers.data)
        else:
            return Response({"response": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def post(request, pk):
        data = request.data
        serializers = RatePostSerializers(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response({"response": "Success"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"response": "Serialize Error"}, status=status.HTTP_400_BAD_REQUEST)


class RateShareView(APIView):
    @staticmethod
    def get(request, pk):
        rate = get_object_or_404(SnRateShare, pk=pk)
        if rate:
            serializers = RateShareSerializers(rate)
            return Response(serializers.data)
        else:
            return Response({"response": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def post(request, pk):
        data = request.data
        serializers = RateShareSerializers(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response({"response": "Success"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"response": "Serialize Error"}, status=status.HTTP_400_BAD_REQUEST)


class RatePostCommentView(APIView):
    @staticmethod
    def get(request, pk):
        rate = get_object_or_404(SnRatePostComment, pk=pk)
        if rate:
            serializers = RatePostCommentSerializers(rate)
            return Response(serializers.data)
        else:
            return Response({"response": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def post(request, pk):
        data = request.data
        serializers = RatePostCommentSerializers(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response({"response": "Success"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"response": "Serialize Error"}, status=status.HTTP_400_BAD_REQUEST)


class RatePostReplayView(APIView):
    @staticmethod
    def get(request, pk):
        rate = get_object_or_404(SnRatePostReplay, pk=pk)
        if rate:
            serializers = RatePostReplaySerializers(rate)
            return Response(serializers.data)
        else:
            return Response({"response": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def post(request, pk):
        data = request.data
        serializers = RatePostReplaySerializers(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response({"response": "Success"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"response": "Serialize Error"}, status=status.HTTP_400_BAD_REQUEST)


class RateShareCommentView(APIView):
    @staticmethod
    def get(request, pk):
        rate = get_object_or_404(SnRateShareComment, pk=pk)
        if rate:
            serializers = RateShareCommentSerializers(rate)
            return Response(serializers.data)
        else:
            return Response({"response": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def post(request, pk):
        data = request.data
        serializers = RateShareCommentSerializers(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response({"response": "Success"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"response": "Serialize Error"}, status=status.HTTP_400_BAD_REQUEST)


class RateShareReplayView(APIView):
    @staticmethod
    def get(request, pk):
        rate = get_object_or_404(SnRateShareReplay, pk=pk)
        if rate:
            serializers = RateShareReplaySerializers(rate)
            return Response(serializers.data)
        else:
            return Response({"response": "Bad Request"}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def post(request, pk):
        data = request.data
        serializers = RateShareReplaySerializers(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response({"response": "Success"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"response": "Serialize Error"}, status=status.HTTP_400_BAD_REQUEST)

