from rest_framework import serializers
from .models import Shirt, Pant

class ShirtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shirt
        fields = ['id', 'name', 'image']

class PantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pant
        fields = ['id', 'name', 'image']
