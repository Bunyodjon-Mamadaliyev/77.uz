from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Address, Seller, User


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["name", "lat", "lng"]


class UserSerializer(serializers.ModelSerializer):
    address = serializers.PrimaryKeyRelatedField(queryset=Address.objects.all(), write_only=True)
    address_detail = AddressSerializer(source="address", read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "full_name",
            "phone_number",
            "profile_photo",
            "address",
            "address_detail",
            "created_at",
        ]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password_confirm = serializers.CharField(write_only=True)
    address_detail = AddressSerializer(write_only=True)
    access_token = serializers.SerializerMethodField()
    refresh_token = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "full_name",
            "phone_number",
            "password",
            "password_confirm",
            "profile_photo",
            "address_detail",
            "access_token",
            "refresh_token",
            "user",
        ]
        extra_kwargs = {"profile_photo": {"required": False, "allow_null": True}}

    def validate(self, data):
        if data["password"] != data["password_confirm"]:
            raise serializers.ValidationError("Parollar mos emas.")
        return data

    def create(self, validated_data):
        address_data = validated_data.pop("address_detail")
        password = validated_data.pop("password")
        validated_data.pop("password_confirm")
        address = Address.objects.create(**address_data)
        user = User.objects.create(address=address, **validated_data)
        user.set_password(password)
        user.save()
        return user

    def get_tokens(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }

    def get_access_token(self, obj):
        tokens = self.get_tokens(obj)
        return tokens["access"]

    def get_refresh_token(self, obj):
        tokens = self.get_tokens(obj)
        return tokens["refresh"]

    def get_user(self, obj):
        return {
            "id": obj.id,
            "full_name": obj.full_name,
            "phone_number": obj.phone_number,
            "profile_photo": (obj.profile_photo.url if obj.profile_photo else None),
            "address_detail": {
                "name": obj.address.name,
                "lat": obj.address.lat,
                "lng": obj.address.lng,
            },
            "created_at": obj.created_at,
        }


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        phone = data.get("phone_number")
        password = data.get("password")
        user = authenticate(phone_number=phone, password=password)
        if not user:
            raise serializers.ValidationError("Noto‘g‘ri foydalanuvchi nomi yoki parol")
        refresh = RefreshToken.for_user(user)
        return {
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
            "user": {
                "id": user.id,
                "full_name": user.full_name,
                "phone_number": user.phone_number,
            },
        }


class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "full_name",
            "phone_number",
            "profile_photo",
            "address",
        )
        read_only_fields = ("profile_photo",)


class SellerRegistrationSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Seller
        fields = (
            "id",
            "full_name",
            "project_name",
            "category",
            "phone_number",
            "address",
        )
        read_only_fields = ("id",)

    def create(self, validated_data):
        address_data = validated_data.pop("address")
        address = Address.objects.create(**address_data)
        registration = Seller.objects.create(address=address, **validated_data, status="pending")
        return registration
