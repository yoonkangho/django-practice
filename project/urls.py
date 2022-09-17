# built-in imports

# third party imports
from django.contrib import admin
from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.authtoken import views as AuthTokenView

# application imports


urlpatterns = [
    path("admin", admin.site.urls),
    path("auth", AuthTokenView.obtain_auth_token),
    # drf-spectacular
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("schema/redoc/", SpectacularRedocView.as_view(url_name="schema")),
    path("schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema")),
]
