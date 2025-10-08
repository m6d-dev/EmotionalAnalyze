from rest_framework import serializers
from src.apps.emotions.service import emotions_service

class PostEmotionsSerializer(serializers.Serializer):
    images = serializers.FileField()

