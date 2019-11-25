from rest_framework import serializers
from .models import SnAlbum, SnContentDetail, VisibilityMode, SnContentType
from timeline.models import Post
from timeline.serializers import PostSerializers
from user.serializers import UserSerializer


class AlbumSerializers(serializers.ModelSerializer):
    class Meta:
        model = SnAlbum
        fields = '__all__'


class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnContentType
        fields = '__all__'


class ContentSerializerPost(serializers.ModelSerializer):

    class Meta:
        model = SnContentDetail
        fields = '__all__'


class VisibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = VisibilityMode
        fields = '__all__'

# for reverse call. in one to many field call from from one side.... (testing)

# class ContentSerializer(serializers.ModelSerializer):
#     # post = PostSerializers()
#     user = UserSerializer()
#     visibility_mode = VisibilitySerializer()
#     #album = AlbumSerializers()
#     # content_type = ContentTypeSerializer()
#     post_content_reverse = ContentSerializerPost(many=True, read_only=True)
#     print(post_content_reverse.data)
#
#     class Meta:
#         #model = SnContentDetail
#         model = Post
#         #fields = ['is_featured', 'is_captcha', 'file', 'content_type', 'album', 'post', 'user']
#         fields = ['id', 'post_text', 'post_date', 'user', 'visibility_mode', 'post_content_reverse']


class ContentSerializer(serializers.ModelSerializer):
    post = PostSerializers()
    user = UserSerializer()
    album = AlbumSerializers()
    content_type = ContentTypeSerializer()

    class Meta:
        model = SnContentDetail
        fields = ['is_featured', 'is_captcha', 'file', 'content_type', 'album', 'post', 'user']


class ReactCountSerializer(serializers.ModelSerializer):
    post = serializers.CharField()
    total = serializers.IntegerField()
