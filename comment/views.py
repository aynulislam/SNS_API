from rest_framework.views import APIView, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import PostComment, PostReply, ShareComment, ShareReply
from .serializers import PostCommentSerializer, PostReplySerializer, ShareCommentSerializer, ShareReplySerializer


class PostCommentApiView(APIView):
    @staticmethod
    def get(request, pk):
        comments = PostComment.objects.all().filter(post=pk)
        if comments:
            serializer = PostCommentSerializer(comments, many=True)
            return Response(serializer.data)
        else:
            content = {
                'status': 'request was not permitted'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    @staticmethod
    def post(request, pk=0):
        data = request.data
        serializer = PostCommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "Success"}, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response({"response": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

    @staticmethod
    def patch(request, pk=0):
        data = request.data
        comment = get_object_or_404(PostComment, pk=data['id'])
        serializer = PostCommentSerializer(comment, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "Success"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"response": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

    @staticmethod
    def delete(request, pk):
        get_comment = get_object_or_404(PostComment, pk=pk)
        get_comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostReplyApiView(APIView):
    @staticmethod
    def get(request, pk):
        comments = PostReply.objects.all().filter(post=pk)
        if comments:
            serializer = PostReplySerializer(comments, many=True)
            return Response(serializer.data)
        else:
            content = {
                'status': 'request was not permitted'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    @staticmethod
    def post(request, pk=0):
        data = request.data
        serializer = PostReplySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "Success"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"response": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

    @staticmethod
    def patch(request, pk=0):
        data = request.data
        comment = get_object_or_404(PostComment, pk=data['id'])
        serializer = PostReplySerializer(comment, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "Success"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"response": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

    @staticmethod
    def delete(request, pk):
        get_comment = get_object_or_404(PostComment, pk=pk)
        get_comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ShareCommentApiView(APIView):
    @staticmethod
    def get(request, pk):
        comments = ShareComment.objects.all().filter(post=pk)
        if comments:
            serializer = ShareCommentSerializer(comments, many=True)
            return Response(serializer.data)
        else:
            content = {
                'status': 'request was not permitted'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    @staticmethod
    def post(request, pk=0):
        data = request.data
        serializer = ShareCommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "Success"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"response": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

    @staticmethod
    def patch(request, pk=0):
        data = request.data
        comment = get_object_or_404(PostComment, pk=data['id'])
        serializer = ShareCommentSerializer(comment, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "Success"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"response": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

    @staticmethod
    def delete(request, pk):
        get_comment = get_object_or_404(PostComment, pk=pk)
        get_comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ShareReplyApiView(APIView):
    @staticmethod
    def get(request, pk):
        comments = ShareReply.objects.all().filter(post=pk)
        if comments:
            serializer = ShareReplySerializer(comments, many=True)
            return Response(serializer.data)
        else:
            content = {
                'status': 'request was not permitted'
            }
            return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    @staticmethod
    def post(request, pk=0):
        data = request.data
        serializer = ShareReplySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "Success"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"response": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

    @staticmethod
    def patch(request, pk=0):
        data = request.data
        comment = get_object_or_404(PostComment, pk=data['id'])
        serializer = ShareReplySerializer(comment, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "Success"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"response": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

    @staticmethod
    def delete(request, pk):
        get_comment = get_object_or_404(PostComment, pk=pk)
        get_comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





