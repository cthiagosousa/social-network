from django.contrib.auth import get_user_model
from django.db.models import fields
from rest_framework import serializers

Account = get_user_model()

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'username', 'email', 'bio', 'birth_date', 'profile_picture', 'password', 'password_confirm', 'is_staff', 'is_superuser']
        extra_kwargs = {'password': {'write_only': True}}

        
