from rest_framework import serializers
from .models import Bookmark
from django.urls import reverse

class BookmarkSerializer(serializers.ModelSerializer):
    edit_url = serializers.SerializerMethodField("get_edit_url")

    class Meta:
        model = Bookmark
        fields = ["id", "title", "description", "url", "edit_url", "visits"]

    def get_edit_url(self, bookmark):
        return reverse("bookmark_edit", args=[bookmark.category.id, bookmark.pk])