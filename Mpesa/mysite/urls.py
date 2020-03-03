from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework_jwt.views import obtain_jwt_token
urlpatterns = [
    path('api/v1/', include('mpesa_api.urls')),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_jwt_token, name='create-token'),
    re_path('api/', include('hospitals.urls')),
    re_path('api/', include('users.urls')),
    path('api/password_reset/',
        include('django_rest_passwordreset.urls', namespace='password_reset')),
]