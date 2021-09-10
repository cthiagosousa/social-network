from django.http.request import HttpRequest
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter

from ..serializers.post_serializer import PostSerializer
from ..models import Post

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title']

