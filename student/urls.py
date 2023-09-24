from django.urls import path
from .views import RegisterUser, LoginUser,StudentViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'', StudentViewSet)
urlpatterns = [
    # path('api-token-auth/', TokenObtainPairView.as_view()),
    path('login/', LoginUser.as_view()),
  
    path('api-token-auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterUser.as_view()),
] 
urlpatterns += router.urls
