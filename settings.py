INSTALLED_APPS = [
    ...,
    "rest_framework",
    "corsheaders",
    "rest_framework_simplejwt",
]

MIDDLEWARE = [
    ...,
    "corsheaders.middleware.CorsMiddleware",
]

CORS_ALLOW_ALL_ORIGINS = True  # Для разработки, потом заменить на конкретные домены

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}
Сериализаторы (serializers.py)
python
from rest_framework import serializers
from .models import Blogger, Blog, BlogPlatform, BlogCategory, SubscriberStats

class BlogPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPlatform
        fields = "__all__"

class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = "__all__"

class SubscriberStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriberStats
        fields = ["date", "subscribers", "views"]

class BlogSerializer(serializers.ModelSerializer):
    platform = BlogPlatformSerializer()
    stats = SubscriberStatsSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ["id", "url", "platform", "subscribers_count", "engagement_rate", "stats"]

class BloggerSerializer(serializers.ModelSerializer):
    blogs = BlogSerializer(many=True, read_only=True)
    categories = BlogCategorySerializer(many=True)

    class Meta:
        model = Blogger
        fields = ["id", "name", "bio", "categories", "blogs", "created_at"]
