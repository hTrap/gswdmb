from django.contrib import admin

# Register your models here.
from .models import Post
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    fields = ("published", "title", "slug", "content", "author")
    list_display = ["published", "title", "updated_at"]
    list_display_links = ["title"]
    list_editable = ["published"]
    list_filter = ["published", "updated_at", "author"]
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ["title", "content"]
