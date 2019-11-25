from rest_framework import serializers
from .models import SnAction


class ReactSerializers(serializers.ModelSerializer):
    class Meta:
        model = SnAction
        fields = '__all__'
