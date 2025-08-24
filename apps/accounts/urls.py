from django.urls import path

from .views import (
    CustomTokenRefreshView,
    CustomTokenVerifyView,
    LoginView,
    MeView,
    RegisterView,
    SellerRegistrationView,
    UpdateProfileView,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="account-register"),
    path("login/", LoginView.as_view(), name="login"),
    path(
        "token/refresh/",
        CustomTokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path("token/verify/", CustomTokenVerifyView.as_view(), name="token_verify"),
    path(
        "seller/registration/",
        SellerRegistrationView.as_view(),
        name="seller-registration",
    ),
    path("edit/", UpdateProfileView.as_view(), name="edit-profile"),
    path("me/", MeView.as_view(), name="me"),
]
