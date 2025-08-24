from rest_framework import serializers

from apps.accounts.models import Address

from .models import (
    Ad,
    AdImage,
    Category,
    FavouriteProduct,
    MySearch,
    PopularSearchTerm,
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "parent", "icon"]


class CategoryWithChildrenSerializer(serializers.ModelSerializer):
    children = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "icon", "children"]


class AddressSerializer(serializers.ModelSerializer):
    def validate_latitude(self, value):
        if not (-90 <= value <= 90):
            raise serializers.ValidationError("Latitude must be between -90 and 90.")
        return value

    def validate_longitude(self, value):
        if not (-180 <= value <= 180):
            raise serializers.ValidationError("Longitude must be between -180 and 180.")
        return value

    class Meta:
        model = Address
        fields = ["name", "lat", "lng"]


class AdImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdImage
        fields = ["id", "image", "is_main"]


class AdSerializer(serializers.ModelSerializer):
    photos = AdImageSerializer(many=True, read_only=True)
    photo = serializers.SerializerMethodField()
    seller = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Ad
        fields = [
            "id",
            "name",
            "slug",
            "description",
            "price",
            "photos",
            "photo",
            "published_at",
            "address",
            "seller",
            "category",
            "is_liked",
            "view_count",
            "updated_time",
        ]

    def get_photo(self, obj):
        main_image = obj.photos.filter(is_main=True).first()
        return main_image.image.url if main_image else None

    def get_seller(self, obj):
        return {
            "id": obj.seller.id,
            "full_name": obj.seller.get_full_name(),
            "phone_number": obj.seller.phone_number,
            "profile_photo": (obj.seller.profile_photo.url if obj.seller.profile_photo else None),
        }

    def get_is_liked(self, obj):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            return obj.favouriteproduct_set.filter(user=request.user).exists()
        device_id = request.query_params.get("device_id") if request else None
        if device_id:
            return obj.favouriteproduct_set.filter(device_id=device_id).exists()
        return False


class MyAdSerializer(AdSerializer):
    status = serializers.CharField(read_only=True)

    class Meta(AdSerializer.Meta):
        fields = AdSerializer.Meta.fields + ["status"]


class AdCreateSerializer(serializers.ModelSerializer):
    photos = serializers.ListField(child=serializers.URLField(), write_only=True, required=True)

    class Meta:
        model = Ad
        fields = ["name", "category", "description", "price", "photos"]

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Narx 0 dan katta bo'lishi kerak.")
        return value

    def create(self, validated_data):
        photos = validated_data.pop("photos", [])
        request = self.context.get("request")

        if not request or not request.user.is_authenticated:
            raise serializers.ValidationError("Foydalanuvchi aniqlanmadi.")

        ad = Ad.objects.create(seller=request.user, **validated_data)
        for i, photo_url in enumerate(photos):
            AdImage.objects.create(ad=ad, image=photo_url, is_main=(i == 0))
        return ad

    def get_seller(self, obj):
        return {
            "id": obj.seller.id,
            "full_name": obj.seller.full_name,
            "phone_number": obj.seller.phone_number,
        }


class FavouriteProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavouriteProduct
        fields = ["id", "product", "device_id", "created_at"]
        extra_kwargs = {
            "device_id": {"required": False},
            "user": {"required": False},
        }

    def create(self, validated_data):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            validated_data["user"] = request.user
        return super().create(validated_data)


class MySearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = MySearch
        fields = [
            "id",
            "category",
            "search_query",
            "price_min",
            "price_max",
            "region_id",
            "created_at",
        ]

    def validate(self, data):
        min_price = data.get("price_min")
        max_price = data.get("price_max")
        if min_price and max_price and min_price > max_price:
            raise serializers.ValidationError("Minimal narx maksimal narxdan katta bo'lmasligi kerak.")
        return data

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)


class PopularSearchTermSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularSearchTerm
        fields = ["id", "name", "icon", "search_count"]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep["search_count"] = f"{rep['search_count']} ta qidiruv"
        return rep
