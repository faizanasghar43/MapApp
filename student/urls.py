from django.urls import path
from .views import RegisterUser, LoginUser
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # path('api-token-auth/', TokenObtainPairView.as_view()),
    path('login/', LoginUser.as_view()),

    path('api-token-auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterUser.as_view()),
]
