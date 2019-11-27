from rest_framework import serializers
from .models import SnPostView, SnShareView


class PostViewSerializers(serializers.ModelSerializer):
    class Meta:
        model = SnPostView
        fields = '__all__'


class ShareViewSerializers(serializers.ModelSerializer):
    class Meta:
        model = SnShareView
        fields = '__all__'

