from django.contrib import admin
from .models import MediaItem, Category  # Update this line to import MediaItem

admin.site.register(MediaItem)
admin.site.register(Category)