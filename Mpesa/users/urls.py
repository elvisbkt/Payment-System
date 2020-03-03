from django.urls import path, include
from .views import LoginView, RegisterUsersView, UserViewSet, UsersList, UserDetail, ProfilesDetail, ProfilesList
from rest_framework import routers
from rest_framework_jwt.views import refresh_jwt_token
router = routers.DefaultRouter()


router.register('users', UserViewSet)

urlpatterns = [
    path('auth/refresh-token/', refresh_jwt_token),
    path('auth/login/', LoginView.as_view(), name="auth-login"),
    path('auth/register/', RegisterUsersView.as_view(), name="auth-register"),
    path('users/', UsersList.as_view(), name="list-all-users"),
    path('user/<int:pk>/', UserDetail.as_view(), name="details-one-user"),
    path('', include(router.urls)),
    path('profile/', ProfilesList.as_view(), name='list_or_create_new_profile'),
    path('profile/<int:pk>/', ProfilesDetail.as_view(), name='get,patch,put,delete profile'),
]