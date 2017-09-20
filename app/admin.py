from django.contrib import admin
from .models import Post
from django.utils import timezone
from django.contrib.admin import SimpleListFilter
from .forms import PostForm

# Register your models here.
def make_published(modeladmin, request, queryset):
    queryset.update(published_date = timezone.now())
make_published.short_description = "Mark selected posts as published"


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_date']
    ordering = ['title']
    action = [make_published]
    list_filter = []

# class PostAdmin(admin.ModelAdmin):
#     form = PostForm
#     # regular stuff
#     class Media:
#         js = (
#             'https://cloud.tinymce.com/stable/tinymce.min.js' # tinymce js file
#             'js/myscript.js',       # project static folder
#         )

admin.site.register(Post, PostAdmin)