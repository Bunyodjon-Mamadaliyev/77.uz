from django.contrib import admin

from .models import (
    Ad,
    AdImage,
    Category,
    FavouriteProduct,
    MySearch,
    PopularSearchTerm,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "parent", "icon")
    search_fields = ("name",)
    list_filter = ("parent",)


class AdImageInline(admin.TabularInline):
    model = AdImage
    extra = 1


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "price",
        "status",
        "category",
        "seller",
        "view_count",
        "published_at",
    )
    search_fields = ("name", "description", "slug")
    list_filter = ("status", "category", "published_at")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [AdImageInline]
    autocomplete_fields = ("category", "seller", "address")


@admin.register(AdImage)
class AdImageAdmin(admin.ModelAdmin):
    list_display = ("id", "ad", "image", "is_main")
    list_filter = ("is_main",)
    search_fields = ("ad__name",)


@admin.register(FavouriteProduct)
class FavouriteProductAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "device_id", "product", "created_at")
    search_fields = ("user__username", "device_id", "product__name")
    list_filter = ("created_at",)


@admin.register(MySearch)
class MySearchAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "category",
        "search_query",
        "price_min",
        "price_max",
        "region_id",
        "created_at",
    )
    search_fields = ("search_query", "user__username")
    list_filter = ("category", "created_at")


@admin.register(PopularSearchTerm)
class PopularSearchTermAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "search_count", "updated_at")
    search_fields = ("name",)
    list_filter = ("category",)
