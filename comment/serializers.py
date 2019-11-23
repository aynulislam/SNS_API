from rest_framework import serializers

from .models import PostComment, PostReply, ShareComment, ShareReply


class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = "__all__"


class PostReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostReply
        fields = "__all__"


class ShareCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShareComment
        fields = "__all__"


class ShareReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = ShareReply
        fields = "__all__"


