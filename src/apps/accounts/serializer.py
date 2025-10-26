from rest_framework import serializers

from src.apps.accounts.models import User

class RegisterSerialzier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "password"
        )
