from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import RefreshToken, UntypedToken
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from .models import Seller
from .serializers import (
    LoginSerializer,
    RegisterSerializer,
    SellerRegistrationSerializer,
    UpdateProfileSerializer,
)

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        return Response(
            {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "user": {
                    "id": user.id,
                    "full_name": user.full_name,
                    "phone_number": user.phone_number,
                    "profile_photo": (
                        request.build_absolute_uri(user.profile_photo.url) if user.profile_photo else None
                    ),
                    "address_detail": {
                        "name": user.address.name,
                        "lat": user.address.lat,
                        "lng": user.address.lng,
                    },
                    "created_at": user.created_at,
                },
            },
            status=status.HTTP_201_CREATED,
        )


class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            return Response(
                {"access_token": response.data["access"]},
                status=status.HTTP_200_OK,
            )
        return response


class CustomTokenVerifyView(TokenVerifyView):
    def post(self, request, *args, **kwargs):
        token = request.data.get("token")
        try:
            validated_token = UntypedToken(token)
            user_id = validated_token["user_id"]
            return Response({"valid": True, "user_id": user_id}, status=status.HTTP_200_OK)
        except (InvalidToken, TokenError):
            return Response(
                {
                    "detail": "Token noto‘g‘ri yoki muddati tugagan",
                    "code": "token_not_valid",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        access_token = data["access_token"]
        refresh_token = data["refresh_token"]
        response = Response(
            {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "user": data["user"],
            },
            status=200,
        )
        response.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,
            secure=False,
            samesite="Lax",
            max_age=60 * 60,
        )
        response.set_cookie(
            key="refresh_token",
            value=refresh_token,
            httponly=True,
            secure=False,
            samesite="Lax",
            max_age=60 * 60 * 24,
        )
        return response


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        return Response(
            {
                "id": user.id,
                "full_name": user.full_name,
                "phone_number": user.phone_number,
                "profile_photo": (request.build_absolute_uri(user.profile_photo.url) if user.profile_photo else None),
                "address": {
                    "name": user.address.name if user.address else None,
                    "lat": user.address.lat if user.address else None,
                    "long": user.address.lng if user.address else None,
                },
            }
        )


class UpdateProfileView(generics.UpdateAPIView):
    serializer_class = UpdateProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class SellerRegistrationView(generics.CreateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerRegistrationSerializer
    permission_classes = [permissions.AllowAny]
