from rest_framework import serializers
from .models import SnReactPost, SnReactShare


class ReactPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = SnReactPost
        fields = '__all__'


class ShareSerializers(serializers.ModelSerializer):
    class Meta:
        model = SnReactShare
        fields = '__all__'

