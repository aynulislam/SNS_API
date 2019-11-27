from psycopg2._psycopg import IntegrityError
from django.db.models import Prefetch
from rest_framework.parsers import MultiPartParser, FileUploadParser, FormParser, JSONParser
from rest_framework.exceptions import NotAcceptable
from django.forms.models import model_to_dict
from rest_framework.views import APIView, status
from .models import Post
from .serializers import PostSerializers
from django.core import serializers
from content.serializers import ContentSerializer, ContentSerializerPost
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db import transaction
from django.shortcuts import get_object_or_404


# for testing using prefetch and reverse relation :: http://bit.ly/2WMNG9r
class PostList(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        #posts = Post.objects.prefetch_related(Prefetch('post_content_reverse')).post_content_reverse.all()
        posts = Post.objects.prefetch_related(Prefetch('post_content_reverse')).all()
        print(posts)
        return Response(ContentSerializer(posts, many=True).data, status.HTTP_201_CREATED)
        # post_list = []
        # i = 0
        # for post in posts:
        #     post_obj = post.post_content_reverse.all()
        #     post_data = model_to_dict(post_obj)
        #     print(post_data)
        #     #ser = ContentSerializer(, many=True)
        #     #serialized_obj = serializers.serialize('json', [post.post_content_reverse.all(), ])
        #     #print(json.dumps(post_obj))
        # return Response(serializers.serialize('json', post_obj), status.HTTP_200_OK)


class PostApi(APIView):
    permission_classes = [IsAuthenticated]
    parser_class = (MultiPartParser,)

    @transaction.atomic
    def post(self, request):
        try:
            data = request.data
            post_data = {"user": request.user.id, "post_text": data["post_text"],
                         "visibility_mode": data["visibility_mode"]}
            serializer = PostSerializers(data=post_data)
            if serializer.is_valid():
                post_object = serializer.save()
                files = request.data.getlist('content')
                if len(files) == 0:
                    file_data = {'content_type': data['content_type'], 'user': request.user.id,
                                 'album': data['album'], 'is_featured': data['is_featured'],
                                 'is_captcha': data['is_captcha'], 'post': post_object.id, 'file': None}
                    print(file_data)
                    ser_content = ContentSerializerPost(data=file_data)
                    if ser_content.is_valid():
                        ser_content.save()
                    else:
                        print(ser_content.errors)
                        raise NotAcceptable('Save Error')
                if files:
                    for file in files:
                        file_data = {'content_type': data['content_type'], 'user': request.user.id,
                                     'album': data['album'], 'is_featured': data['is_featured'],
                                     'is_captcha': data['is_captcha'], 'post': post_object.id, 'file': file}
                        print(file_data)
                        ser_content = ContentSerializerPost(data=file_data)
                        if ser_content.is_valid():
                            ser_content.save()
                        else:
                            raise NotAcceptable('Save Error')

                return Response({"response": "Success"}, status=status.HTTP_201_CREATED)
            else:
                raise NotAcceptable('Save Error')
        except IntegrityError:
            raise NotAcceptable('Save Error')

    @transaction.atomic
    def patch(self, request):
        data = request.data
        serializers = PostSerializers(data=data, partial=True)
        if serializers.is_valid():
            obj = serializers.save()
            data1 = data["content"]
            for d in data1:
                d["post"] = obj.id
                print(d)
                ser_content = ContentSerializer(d, partial=True)
                if ser_content.is_valid():
                    ser_content.save()
                else:
                    return Response({"response": "Save Error"}, status=status.HTTP_400_BAD_REQUEST)

            return Response({"response": "Success"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"response": "Serialize Error"}, status=status.HTTP_400_BAD_REQUEST)


class PostDetails(APIView):
    def get(self, request, pk):
        post_get = get_object_or_404(Post, pk=pk)
        if post_get:
            serializers = PostSerializers(data=post_get)
            if serializers.is_valid():
                return Response(serializers.data)
            else:
                content = {
                    'status': 'request was not permitted..'
                }
                return Response(content, status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, pk):
        post_get = get_object_or_404(Post, pk=pk)
        post_get.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
