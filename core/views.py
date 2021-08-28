from django.http.request import HttpRequest
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from .serializers.account_serializer import AccountSerializer
from . serializers.post_serializer import PostSerializer
from .models import Post

Account = get_user_model()

class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
