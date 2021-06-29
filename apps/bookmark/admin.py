from django.contrib import admin

# Register your models here.
from .models import Bookmark, Category

admin.site.register(Category)
admin.site.register(Bookmark)
