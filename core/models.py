from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    username = models.CharField(max_length=100, unique=True, null=False, blank=False)
    email = models.EmailField(max_length=100, unique=True, null=False, blank=False)
    bio = models.TextField(max_length=150, null=True, blank=True)
    birth_date = models.DateField(blank=False, null=False)
    profile_picture = models.ImageField(null=True, blank=True)

    class Meta:
        db_table = 'accounts'
    
    def __str__(self) -> str:
        return self.username

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False, editable=False)
    updated_at = models.DateTimeField(auto_now=True, null=False, blank=False)
    author = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='posts', null=False, blank=False)

    class Meta:
        db_table = 'posts'

    def __str__(self) -> str:
        return self.title
