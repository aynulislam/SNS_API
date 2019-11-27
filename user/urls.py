from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from . import views
from .serializers import CustomJWTSerializer

urlpatterns = [
    path('registration/', views.UserCreate.as_view(), name='registration'),
    path('token/', views.TokenObtainPairView.as_view(serializer_class=CustomJWTSerializer), name='my_token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user/<pk>', views.UserInfoView.as_view(), name="user"),
    path('login_info/', views.UserLoginInfoView.as_view(), name="login_info"),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]
