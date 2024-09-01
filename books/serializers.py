# books/serializers.py
from rest_framework import serializers
from .models import MediaItem, Category, CustomList

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        extra_kwargs = {
            'cover_url': {'read_only': True},  # Example if cover_url should only be set by external data fetching
        }

class MediaItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaItem
        fields = '__all__'

class CustomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomList
        fields = '__all__'
