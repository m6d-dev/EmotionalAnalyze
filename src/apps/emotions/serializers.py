from rest_framework import serializers


class PostEmotionsSerializer(serializers.Serializer):
    images = serializers.FileField()
