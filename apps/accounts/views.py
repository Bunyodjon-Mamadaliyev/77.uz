from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import RefreshToken, UntypedToken
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from .serializers import LoginSerializer, RegisterSerializer

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
                        request.build_absolute_uri(user.profile_photo.url)
                        if user.profile_photo
                        else None
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
            return Response(
                {"valid": True, "user_id": user_id}, status=status.HTTP_200_OK
            )
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
        return Response(serializer.validated_data, status=200)
