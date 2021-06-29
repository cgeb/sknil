from .forms import CategoryForm, BookmarkForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core import serializers
from .serializers import BookmarkSerializer
import json

# Create your views here.
@login_required
def categories(request):
    categories = request.user.categories.all()
    context = {
        "categories": categories
    }
    return render(request, "bookmark/categories.html", context)

@login_required
def category(request, category_id):
    category = request.user.categories.get(pk=category_id)
    bookmarks = BookmarkSerializer(category.bookmarks.all(), many=True)
    context = {
        "category": category,
        "bookmarks": json.dumps(bookmarks.data),
    }
    return render(request, "bookmark/category.html", context)

@login_required
def category_add(request):
    if request.method == "POST":
       form = CategoryForm(request.POST)
       if form.is_valid():
           category = form.save(commit=False)
           category.created_by = request.user
           form.save()

           messages.success(request, "The category has been successfully created.")
           return redirect("categories")
    else:
        form = CategoryForm()

    context = {
        "form": form,
        "userprofile": request.user.userprofile
    }
    return render(request, "bookmark/category_add.html", context)

@login_required
def category_edit(request, category_id):
    category = request.user.categories.get(pk=category_id)

    if request.method == "POST":
       form = CategoryForm(request.POST, instance=category)
       if form.is_valid():
           form.save()

           messages.success(request, "The category has been successfully updated.")
           return redirect("categories")
    else:
        form = CategoryForm(instance=category)

    context = {
        "form": form,
        "category": category
    }
    return render(request, "bookmark/category_edit.html", context)

@login_required
def category_delete(request, category_id):
    category = request.user.categories.get(pk=category_id)
    category.delete()

    messages.success(request, "The category has been successfully deleted.")
    return redirect("categories")


@login_required
def bookmark_add(request, category_id):
    if request.method == "POST":
       form = BookmarkForm(request.POST)
       if form.is_valid():
           bookmark = form.save(commit=False)
           bookmark.category_id = category_id
           bookmark.created_by = request.user
           form.save()

           messages.success(request, "The bookmark has been successfully created.")
           return redirect("category", category_id=category_id)
    else:
        form = BookmarkForm()

    context = {
        "form": form,
        "category_id": category_id,
        "userprofile": request.user.userprofile
    }
    return render(request, "bookmark/bookmark_add.html", context)

@login_required
def bookmark_edit(request, category_id, bookmark_id):
    bookmark = request.user.bookmarks.get(pk=bookmark_id)

    if request.method == "POST":
       form = BookmarkForm(request.POST, instance=bookmark)
       if form.is_valid():
           form.save()

           messages.success(request, "The bookmark has been successfully updated.")
           return redirect("category", category_id=category_id)
    else:
        form = BookmarkForm(instance=bookmark)

    context = {
        "form": form,
        "category_id": category_id,
        "bookmark": bookmark
    }
    return render(request, "bookmark/bookmark_edit.html", context)

@login_required
def bookmark_delete(request, category_id, bookmark_id):
    bookmark = request.user.bookmarks.get(pk=bookmark_id)
    bookmark.delete()

    messages.success(request, "The bookmark has been successfully deleted.")
    return redirect("category", category_id=category_id)
