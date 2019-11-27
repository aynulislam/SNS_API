from rest_framework import serializers
from .models import SnRequest,SnBlock,SnFollow,SnFriend


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnRequest
        fields = '__all__'


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnFriend
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnFollow
        fields = '__all__'


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnBlock
        fields = '__all__'

