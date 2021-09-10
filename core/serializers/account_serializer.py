from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
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
        read_only_fields = ['posts']
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

    def create(self, validated_data: dict) -> Account:
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

    def update(self, instance: Account, validated_data: dict) -> Account:
        self.instance.username = self.validated_data['username']
        self.instance.email = self.validated_data['email']
        self.instance.bio = self.validated_data['bio']
        self.instance.birth_date = self.validated_data['birth_date']
        self.instance.profile_picture = self.validated_data['profile_picture']
        self.instance.is_staff = self.validated_data['is_staff']
        self.instance.is_superuser = self.validated_data['is_superuser']
        password = self.validated_data['password']
        password_confirm = self.validated_data['password_confirm']

        if password != password_confirm:
            raise ValidationError({'error': 'As senhas não são iguais'})

        self.instance.set_password(password)
        self.instance.save()

        return self.instance
