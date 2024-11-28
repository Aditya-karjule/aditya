# api/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UploadedFile
from django.core.signing import Signer
from django.core.mail import send_mail
from django.conf import settings

signer = Signer()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password', 'is_ops_user']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user


class UploadedFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ['file', 'uploaded_by', 'uploaded_at']

class EncryptedDownloadLinkSerializer(serializers.Serializer):
    download_link = serializers.CharField()
