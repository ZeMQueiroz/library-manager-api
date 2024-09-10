# books/migrations/0005_seed_categories.py
from django.db import migrations

def create_categories(apps, schema_editor):
    Category = apps.get_model('books', 'Category')
    # Ensure categories exist with specific IDs
    Category.objects.get_or_create(id=1, defaults={'name': 'Book'})
    Category.objects.get_or_create(id=2, defaults={'name': 'Anime'})

class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_customlist_category_alter_mediaitem_status'),  # Adjust based on your latest migration
    ]

    operations = [
        migrations.RunPython(create_categories),
    ]