from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name="categories", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Bookmark(models.Model):
    class Meta:
        verbose_name_plural = "Bookmarks"
        ordering = ("-visits",)

    category = models.ForeignKey(Category, related_name="bookmarks", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    url = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name="bookmarks", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    visits = models.IntegerField(default=0)

    def __str__(self):
        return self.title
