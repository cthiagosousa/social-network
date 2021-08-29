from django.http.request import HttpRequest
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers.account_serializer import AccountSerializer
from . serializers.post_serializer import PostSerializer
from .models import Post

Account = get_user_model()

class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def update(self, request: HttpRequest, account_id: str) -> Response:
        account = Account.objects.get(id=account_id)
        serializer = AccountSerializer(account, request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'success': 'Conta atualizada.'})
            
        return Response({'error': 'Ocorreu um erro ao atualizar a conta.'})

    def destroy(self, request: HttpRequest, account_id: str) -> Response:
        account = Account.objects.get(id=account_id)
        account.delete()

        return Response({'success': 'Conta deletada.'})

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
