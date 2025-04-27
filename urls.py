from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BloggerViewSet, BlogViewSet, BlogCategoryViewSet

router = DefaultRouter()
router.register(r"bloggers", BloggerViewSet)
router.register(r"blogs", BlogViewSet)
router.register(r"categories", BlogCategoryViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/auth/", include("rest_framework.urls")),  # Для авторизации
]
