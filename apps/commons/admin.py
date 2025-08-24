from django.contrib import admin

from .models import Common, District, Region, Setting


@admin.register(Common)
class CommonAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "created_at", "updated_at")
    search_fields = ("title", "slug")
    list_filter = ("created_at", "updated_at")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "region")
    list_filter = ("region",)
    search_fields = ("name",)


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = (
        "phone",
        "support_email",
        "working_hours",
        "app_version",
        "maintenance_mode",
    )
    list_editable = ("maintenance_mode",)
    search_fields = ("phone", "support_email", "app_version")
