from django.contrib import admin
from django.urls import path, include

from . import swagger


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/emotions/", include("src.apps.emotions.urls")),
]

urlpatterns += swagger.urlpatterns
