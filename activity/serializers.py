from rest_framework import serializers
from .models import SnActivity


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SnActivity
        fields = '__all__'
