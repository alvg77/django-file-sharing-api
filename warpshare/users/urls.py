from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("signin/", views.LoginView.as_view(), name="signin"),
    path("<int:id>/", views.getUser, name="user"),
    path("util/", views.UpdateDeleteUserView.as_view(), name="user_util"),
    path("jwt/create/", TokenObtainPairView.as_view(), name="jwt_create"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt_verify"),
]
