from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView,
)

from user.views import (
    CreateUserView,
    ManageUserView,
    UserListView,
    UserDetailView,
)

app_name = "user"


urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("logout/", TokenBlacklistView.as_view(), name="logout"),
    path("me/", ManageUserView.as_view(), name="manage_user"),
    path("users/", UserListView.as_view(), name="users_list"),
    path(
        "<str:username>/",
        UserDetailView.as_view(actions={"get": "retrieve"}),
        name="users-detail",
    ),
]
