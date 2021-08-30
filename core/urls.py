from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from .views import AccountViewSet, PostViewSet

urlpatterns = [
    path('account/', AccountViewSet.as_view({'get': 'get', 'post': 'create'})),
    path('account/<str:account_id>', AccountViewSet.as_view({'get': 'get_by_id', 'put': 'update', 'delete': 'destroy'})),
    path('posts/', PostViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'}))
]

urlpatterns = format_suffix_patterns(urlpatterns)
