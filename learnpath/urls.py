from django.contrib import admin
from django.urls import path, include

# Тут мы пишем адреса для нашего сайта
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("materials.urls", namespace="materials")),
    path("about/", include("about.urls", namespace="about")),
]
