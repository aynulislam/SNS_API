from rest_framework import serializers
from .models import SnVisibility


class VisibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SnVisibility
        fields = '__all__'
