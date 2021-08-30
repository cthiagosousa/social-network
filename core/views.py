from django.http.request import HttpRequest
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers.account_serializer import AccountSerializer
from .serializers.post_serializer import PostSerializer
from .models import Post

Account = get_user_model()

class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_by_id(self, request: HttpRequest, account_id: str) -> Response:
        try:
            account = Account.objects.get(id=account_id)
        except Account.DoesNotExist:
            return Response({'error': 'Conta não encontrada.'})

        serializer = AccountSerializer(account)

        return Response(serializer.data)
    
    def get(self, request: HttpRequest) -> Response:
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)

        return Response(serializer.data)

    def create(self, request: HttpRequest) -> Response:
        serializer = AccountSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)

    def update(self, request: HttpRequest, account_id: str) -> Response:
        try:
            account = Account.objects.get(id=account_id)
        except Account.DoesNotExist:
            return Response({'error': 'Conta não encontrada.'})
        
        serializer = AccountSerializer(account, request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            
        return Response(serializer.errors)

    def destroy(self, request: HttpRequest, account_id: str) -> Response:
        try:
            account = Account.objects.get(id=account_id)
        except Account.DoesNotExist:
            return Response({'error': 'Conta não encontrada.'})

        account.delete()

        return Response({'success': 'Conta deletada.'})

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_by_id(self, requet: HttpRequest, account_id: str) -> Response:
        try:
            post = Post.objects.get(id=account_id)
        except Post.DoesNotExist:
            return Response({'error': 'Postagem não encontrada.'})

        serializer = PostSerializer(post)

        return Response(serializer.data)

    def get(self, request: HttpRequest) -> Response:
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)

        return Response(serializer.data)
    
    def create(self, request: HttpRequest) -> Response:
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)

    def update(self, request: HttpRequest, account_id: str) -> Response:
        try:
            post = Post.objects.get(id=account_id)
        except Post.DoesNotExist:
            return Response({'error': 'Postagem não encontrada'})
        
        serializer = PostSerializer(post, request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    def destroy(self, request: HttpRequest, account_id: str) -> Response:
        try:
            post = Post.objects.get(id=account_id)
        except Post.DoesNotExist:
            return Response({'error': 'Postagem não encontrada.'})
        
        post.delete()
        return Response({'success': 'Postagem deletada.'})
