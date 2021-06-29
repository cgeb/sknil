from apps.bookmark.api import api_bookmark_delete, api_category_delete, api_increase_visits
from django.urls import path
from .views import dashboard, settings
from apps.bookmark.views import bookmark_add, bookmark_delete, bookmark_edit, categories, category, category_add, category_delete, category_edit

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("settings/", settings, name="settings"),
    path("categories/", categories, name="categories"),
    path("categories/add/", category_add, name="category_add"),
    path("categories/<int:category_id>/", category, name="category"),
    path("categories/<int:category_id>/edit/", category_edit, name="category_edit"),
    path("categories/<int:category_id>/delete/", category_delete, name="category_delete"),
    path("categories/<int:category_id>/add_bookmark/", bookmark_add, name="bookmark_add"),
    path("categories/<int:category_id>/edit_bookmark/<int:bookmark_id>/", bookmark_edit, name="bookmark_edit"),
    path("categories/<int:category_id>/delete_bookmark/<int:bookmark_id>/", bookmark_delete, name="bookmark_delete"),

    path("api/categories/<int:category_id>/delete/", api_category_delete, name="api_category_delete"),
    path("api/bookmarks/<int:bookmark_id>/delete/", api_bookmark_delete, name="api_bookmark_delete"),
    path("api/bookmarks/<int:bookmark_id>/increase_visits/", api_increase_visits, name="api_increase_visits")
]