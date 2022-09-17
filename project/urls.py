# built-in imports

# third party imports
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken import views as AuthTokenView

# application imports


urlpatterns = [
    path("admin", admin.site.urls),
    path("auth", AuthTokenView.obtain_auth_token),
]
