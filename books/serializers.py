from rest_framework import serializers
from .models import MediaItem, Category, CustomList

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        extra_kwargs = {
            'cover_url': {'read_only': True},
        }

class MediaItemSerializer(serializers.ModelSerializer):
    # Explicitly define the category field to use PrimaryKeyRelatedField
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = MediaItem
        fields = '__all__'

class CustomListSerializer(serializers.ModelSerializer):
    items = MediaItemSerializer(many=True, read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = CustomList
        fields = '__all__'