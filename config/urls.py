from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("admin/", admin.site.urls),

    # ✅ Schema endpoint (REQUIRED for Swagger)
    path(
        "api/schema/",
        SpectacularAPIView.as_view(),
        name="schema",   # ⭐ VERY IMPORTANT
    ),

    # ✅ Swagger UI
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),

    # Auth APIs
    path("api/auth/register/", include("users.urls")),
    path("api/auth/login/", TokenObtainPairView.as_view()),
    path("api/auth/refresh/", TokenRefreshView.as_view()),

    # Task APIs
    path("api/tasks/", include("tasks.urls")),
]