from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db.models import fields
from rest_framework import serializers

Account = get_user_model()

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = [
            'id', 
            'username', 
            'email', 
            'bio', 
            'birth_date', 
            'profile_picture', 
            'posts', 
            'password', 
            'password_confirm', 
            'is_staff', 
            'is_superuser'
            ]
        extra_kwargs = {'password': {'write_only': True}}

    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        label='Senha'
    )

    password_confirm = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        label='Confirme sua senha'
    )         

    def create(self, validated_data) -> Account:
        username = self.validated_data['username']
        email = self.validated_data['email']
        bio = self.validated_data['bio']
        birth_date = self.validated_data['birth_date']
        profile_picture = self.validated_data['profile_picture']
        password = self.validated_data['password']
        password_confirm = self.validated_data['password_confirm']
        is_staff = self.validated_data['is_staff']
        is_superuser = self.validated_data['is_superuser']

        if password != password_confirm:
            raise ValidationError({'error': 'As senhas não são iguais'})
        
        account = Account.objects.create_user(
            username=username,
            email=email,
            bio=bio,
            birth_date=birth_date,
            profile_picture=profile_picture,
            password=password,
            is_staff=is_staff,
            is_superuser=is_superuser
        )

        return account
