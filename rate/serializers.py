from rest_framework import serializers
from .models import (
    SnRateShare, SnRateShareReplay, SnRatePostReplay,
    SnRateShareComment, SnRatePostComment, SnRatePost
)


class RatePostSerializers(serializers.ModelSerializer):
    class Meta:
        model = SnRatePost
        fields = '__all__'


class RateShareSerializers(serializers.ModelSerializer):
    class Meta:
        model = SnRateShare
        fields = '__all__'


class RatePostCommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = SnRatePostComment
        fields = '__all__'


class RatePostReplaySerializers(serializers.ModelSerializer):
    class Meta:
        model = SnRatePostReplay
        fields = '__all__'


class RateShareCommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = SnRateShareComment
        fields = '__all__'


class RateShareReplaySerializers(serializers.ModelSerializer):
    class Meta:
        model = SnRateShareReplay
        fields = '__all__'
