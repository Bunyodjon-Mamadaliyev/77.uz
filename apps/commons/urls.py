from django.urls import path

from .views import (
    CommonDetailView,
    CommonListView,
    RegionWithDistrictsView,
    SettingView,
)

urlpatterns = [
    path("pages/", CommonListView.as_view(), name="common-pages"),
    path(
        "pages/<slug:slug>/",
        CommonDetailView.as_view(),
        name="common-page-detail",
    ),
    path(
        "regions-with-districts/",
        RegionWithDistrictsView.as_view(),
        name="regions-with-districts",
    ),
    path("setting/", SettingView.as_view(), name="common-setting"),
]
