from django.urls import path

from .views import (
    CustomTokenRefreshView,
    CustomTokenVerifyView,
    LoginView,
    RegisterView,
)

urlpatterns = [
    # path('edit/', UserEditView.as_view(), name='account-edit'),
    path("register/", RegisterView.as_view(), name="account-register"),
    path("login/", LoginView.as_view(), name="login"),
    # path(
    #     "seller/registration/",
    #     SellerRegistrationView.as_view(),
    #     name="seller-registration",
    # )
    path(
        "token/refresh/",
        CustomTokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path(
        "token/verify/", CustomTokenVerifyView.as_view(), name="token_verify"
    ),
    # path('me/', UserProfileView.as_view(), name='user-profile'),
]
