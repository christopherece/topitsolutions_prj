from django.contrib import admin
from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_at', 'category')  # Using fields that exist in the model
    list_filter = ('category', 'published_at')  # Filtering by category and published date
    search_fields = ('title', 'content', 'author')  # Searchable fields
    prepopulated_fields = {'slug': ('title',)}  # Automatically populate the slug field based on the title
    date_hierarchy = 'published_at'  # Use published_at for date-based filtering
    ordering = ('-created_at',)  # Ordering by created_at, newest first

admin.site.register(BlogPost, BlogPostAdmin)
