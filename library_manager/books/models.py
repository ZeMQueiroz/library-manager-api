from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class MediaItem(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[
        ('To Read', 'To Read'),
        ('Reading', 'Reading'),
        ('Finished', 'Finished'),
        ('To Watch', 'To Watch'),
        ('Watching', 'Watching'),
        ('Completed', 'Completed'),
        ('On Hold', 'On Hold')
    ], default='To Read')
    progress = models.IntegerField(default=0)  # e.g., pages read or episodes watched
    rating = models.IntegerField(null=True, blank=True)  # Rating out of 10
    notes = models.TextField(null=True, blank=True)
    cover_url = models.URLField(max_length=200, null=True, blank=True)  # URL for the cover image
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='items')

    def __str__(self):
        return f'{self.title} ({self.category.name})'

    def get_absolute_url(self):
        return reverse('mediaitem_detail', args=[str(self.id)])
    
class CustomList(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    items = models.ManyToManyField('MediaItem', blank=True)  # Relate to MediaItem
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name