from django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    username = models.CharField(max_length=100, unique=True, null=False, blank=False)
    email = models.EmailField(max_length=100, unique=True, null=False, blank=False)
    bio = models.TextField(max_length=150, null=True, blank=True)
    birth_date = models.DateField(blank=False, null=False)
    profile_picture = models.ImageField()

    class Meta:
        db_table = 'accounts'
    
    def __str__(self) -> str:
        return self.username
