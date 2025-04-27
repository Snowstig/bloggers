from django.db import models
from django.contrib.auth.models import User

class BlogPlatform(models.Model):
    name = models.CharField(max_length=50)  # "ВК", "Telegram", "YouTube"
    url_template = models.CharField(max_length=200)  # Шаблон ссылки

    def __str__(self):
        return self.name

class BlogCategory(models.Model):
    name = models.CharField(max_length=100)  # "Кулинария", "IT", "Мода"
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Blogger(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    categories = models.ManyToManyField(BlogCategory)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE, related_name="blogs")
    platform = models.ForeignKey(BlogPlatform, on_delete=models.CASCADE)
    url = models.URLField()
    subscribers_count = models.PositiveIntegerField(default=0)
    engagement_rate = models.FloatField(default=0.0)  # Процент вовлечённости
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.blogger.name} – {self.platform.name}"

class SubscriberStats(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="stats")
    date = models.DateField()
    subscribers = models.PositiveIntegerField()
    views = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.blog} – {self.date}: {self.subscribers}"
