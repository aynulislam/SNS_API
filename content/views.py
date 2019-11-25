from django.http import JsonResponse, HttpResponse
import json
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.views import APIView, status
from django.db.models import  Count
from .serializers import AlbumSerializers, ContentSerializer,\
    ContentTypeSerializer, VisibilitySerializer, ReactCountSerializer
from react.models import SnReactPost
from rest_framework.response import Response
from .models import SnAlbum, SnContentDetail, VisibilityMode, SnContentType
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from django.core import serializers


class AlbumListView(APIView):
    permission_classes = [IsAuthenticated]
    @staticmethod
    def get(request):
        user = request.user
        albums = SnAlbum.objects.all().filter(user=user)
        if albums:
            serializer = AlbumSerializers(albums, many=True)
            return Response(serializer.data)
        else:
            content = {
                'status': 'request was not permitted'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)


class AlbumDetailView(APIView):
    permission_classes = [IsAuthenticated]
    @staticmethod
    def get(request, pk):
        album = get_object_or_404(SnAlbum, pk=pk)
        serializer = AlbumSerializers(data=album)

        if serializer.is_valid():
            return Response(serializer.data)
        else:
            content = {
                'status': 'request was not permitted'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    @staticmethod
    def post(request):
        data = request.data
        serializer = AlbumSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "Success"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"response": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

    @staticmethod
    def patch(request):
        data = request.data
        serializer = AlbumSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "Success"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"response": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

    @staticmethod
    def delete(request, pk):
        instance = get_object_or_404(SnAlbum, pk=pk)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ContentView(APIView):
    permission_classes = [IsAuthenticated]
    @staticmethod
    def get(request, pk):
        data = get_object_or_404(SnContentDetail, pk=pk)
        if data:
            serializer = ContentSerializer(data=data)
            if serializer.is_valid():
                return Response(serializer.data)
            else:
                content = {
                        'status': 'request was not permitted'
                    }
                return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    @staticmethod
    def post(request, pk='None'):
        data = request.data
        if data:
            serializer = ContentSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"response": "Success"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"response": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

    @staticmethod
    def delete(request, pk):
        content = get_object_or_404(SnContentDetail, pk=pk)
        content.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VisibilityListView(APIView):
    permission_classes = [IsAuthenticated]
    @staticmethod
    def get(request):
        visibility = VisibilityMode.objects.all()
        if visibility:
            serializer = VisibilitySerializer(visibility, many=True)
            return Response(serializer.data)
        else:
            content = {
                'status': 'request was not permitted'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)


class ContentTypeView(APIView):
    @staticmethod
    def get(request):
        content_type = SnContentType.objects.all()
        serializer = ContentTypeSerializer(content_type, many=True)
        if serializer:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            content = {
                'status': 'Not found'
            }
            return Response(content, status=status.HTTP_404_NOT_FOUND)


class PostContent(APIView):
    permission_classes = [IsAuthenticated]
    @staticmethod
    def get(request):
        posts = SnContentDetail.objects.select_related('post', 'user', 'content_type', 'album')
        serializer = ContentSerializer(posts, many=True)
        count = SnReactPost.objects.all().values('post', 'react_type').annotate(total=Count('react_type'))
        return Response({"post": serializer.data, "react": count}, status=status.HTTP_200_OK)
