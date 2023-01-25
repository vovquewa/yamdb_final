from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, register, get_jwt_token
from .views import (CategoriesViewSet,
                    GenreViewSet,
                    TitleViewSet,
                    ReviewViewset,
                    CommentViewset
                    )

v1_router = DefaultRouter()

v1_router.register('users', UserViewSet)
v1_router.register('categories', CategoriesViewSet)
v1_router.register('genres', GenreViewSet)
v1_router.register('titles', TitleViewSet)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewset,
    basename='review'
)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewset, basename='comment')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/auth/signup/', register, name='register'),
    path('v1/auth/token/', get_jwt_token, name='token'),
]
