from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    AdViewSet,
    CategoryViewSet,
    CategoryWithChildrenView,
    FavouriteProductViewSet,
    MyAdViewSet,
    MySearchViewSet,
    PopularSearchTermView,
    ProductDownloadView,
    ProductImageCreateView,
    SearchCompleteView,
    SearchCountIncreaseView,
)

router = DefaultRouter()
router.register(r"category", CategoryViewSet, basename="category")
router.register(r"ads", AdViewSet, basename="ads")
router.register(r"my-ads", MyAdViewSet, basename="my-ads")
router.register(r"favourite-product", FavouriteProductViewSet, basename="favourite-product")
router.register(r"my-search", MySearchViewSet, basename="my-search")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "categories-with-childs/",
        CategoryWithChildrenView.as_view(),
        name="categories-with-childs",
    ),
    path(
        "sub-category/",
        CategoryViewSet.as_view({"get": "list"}),
        name="sub-category",
    ),
    path("list/ads/", AdViewSet.as_view({"get": "list"}), name="ads-list"),
    path(
        "my-favourite-product/",
        FavouriteProductViewSet.as_view({"get": "list"}),
        name="my-favourite-product",
    ),
    path(
        "my-favourite-product-by-id/",
        FavouriteProductViewSet.as_view({"get": "list"}),
        name="my-favourite-product-by-id",
    ),
    path(
        "favourite-product-by-id/<int:id>/delete/",
        FavouriteProductViewSet.as_view({"delete": "destroy"}),
        name="favourite-product-by-id-delete",
    ),
    path(
        "favourite-product/<int:id>/delete/",
        FavouriteProductViewSet.as_view({"delete": "destroy"}),
        name="favourite-product-delete",
    ),
    path(
        "my-search/list/",
        MySearchViewSet.as_view({"get": "list"}),
        name="my-search-list",
    ),
    path(
        "my-search/<int:id>/delete/",
        MySearchViewSet.as_view({"delete": "destroy"}),
        name="my-search-delete",
    ),
    path(
        "search/populars/",
        PopularSearchTermView.as_view(),
        name="search-populars",
    ),
    path(
        "search/count-increase/<int:id>/",
        SearchCountIncreaseView.as_view(),
        name="search-count-increase",
    ),
    path(
        "search/complete/",
        SearchCompleteView.as_view(),
        name="search-complete",
    ),
    path(
        "search/category-product/",
        SearchCompleteView.as_view(),
        name="search-category-product",
    ),
    path(
        "product-download/<slug:slug>/",
        ProductDownloadView.as_view(),
        name="product-download",
    ),
    path(
        "product-image-create/",
        ProductImageCreateView.as_view(),
        name="product-image-create",
    ),
]
