from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "password",
        ]
        read_only_fields = ["id"]

    def validate_password(self, value):
        if not len(value) >= 8:
            raise serializers.ValidationError("Password is to short")

        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
