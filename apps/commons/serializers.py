from rest_framework import serializers

from .models import Common, District, Region, Setting


class CommonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Common
        fields = ("slug", "title_uz", "title_ru")


class CommonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Common
        fields = [
            "id",
            "slug",
            "title_uz",
            "title_ru",
            "content",
            "created_at",
            "updated_at",
        ]


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ["id", "name_uz", "name_ru"]


class RegionWithDistrictSerializer(serializers.ModelSerializer):
    districts = DistrictSerializer(many=True, read_only=True)

    class Meta:
        model = Region
        fields = ["id", "name_uz", "name_ru", "districts"]


class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = [
            "id",
            "phone",
            "support_email",
            "working_hours",
            "app_version",
            "maintenance_mode",
        ]
