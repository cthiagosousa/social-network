from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.account_viewset import AccountViewSet
from .views.post_viewset import PostViewSet

router = DefaultRouter()
router.register('account', AccountViewSet, basename='account')
router.register('posts', PostViewSet, basename='posts')

urlpatterns = [
    path('', include(router.urls))
]
