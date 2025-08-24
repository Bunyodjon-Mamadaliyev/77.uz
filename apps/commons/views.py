from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.common.pagination import CustomPagination

from .models import Common, Region, Setting
from .serializers import (
    CommonDetailSerializer,
    CommonListSerializer,
    RegionWithDistrictSerializer,
    SettingSerializer,
)


class CommonListView(generics.ListAPIView):
    queryset = Common.objects.all()
    serializer_class = CommonListSerializer
    permission_classes = [AllowAny]


class CommonDetailView(generics.RetrieveAPIView):
    queryset = Common.objects.all()
    serializer_class = CommonDetailSerializer
    lookup_field = "slug"
    permission_classes = [AllowAny]


class RegionWithDistrictsView(generics.ListAPIView):
    queryset = Region.objects.all().prefetch_related("districts").order_by("name")
    serializer_class = RegionWithDistrictSerializer
    pagination_class = CustomPagination
    permission_classes = [AllowAny]


class SettingView(APIView):
    def get(self, request):
        setting = Setting.objects.first()
        serializer = SettingSerializer(setting)
        return Response(serializer.data)
