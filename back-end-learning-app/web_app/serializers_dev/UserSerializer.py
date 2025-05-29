from rest_framework.serializers import ModelSerializer
from web_app.models import User
from django.utils.html import escape
from rest_framework import serializers




class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'full_name', 'phone', 'created_at', 'updated_at', 'password')
        read_only_fields = ['id', 'created_at', 'updated_at']
        extra_kwargs = {
            'username': {'required': True},
            'email': {'required': True},
            'full_name': {'required': True},
            'password': {'required': True, 'write_only': True}
        }

    #* It prevent all XSS attacks, when detect a XSS attack, it will return a 400 error using escape() function
    def validate(self, attrs):
        # Escape all string fields to prevent XSS
        for field, value in attrs.items():
            if isinstance(value, str):
                attrs[field] = escape(value)
        return attrs



