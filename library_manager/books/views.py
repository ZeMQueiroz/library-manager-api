from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import MediaItem, Category, CustomList
from .serializers import MediaItemSerializer, CategorySerializer, CustomListSerializer
from .utils import fetch_book_info, fetch_anime_info
import random

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class MediaItemListCreateView(generics.ListCreateAPIView):
    queryset = MediaItem.objects.all()
    serializer_class = MediaItemSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'status']
    search_fields = ['title', 'description']
    ordering_fields = ['title', 'rating', 'progress']

    def perform_create(self, serializer):
        category = serializer.validated_data.get('category')
        title = serializer.validated_data.get('title')

        if category.name == 'Anime':
            anime_info = fetch_anime_info(title)
            if anime_info:
                # Ensure only valid fields are passed to the save method
                valid_data = {key: value for key, value in anime_info.items() if key in serializer.fields}
                serializer.save(**valid_data)
            else:
                serializer.save()
        elif category.name == 'Book':
            book_info = fetch_book_info(title)
            if book_info:
                valid_data = {key: value for key, value in book_info.items() if key in serializer.fields}
                serializer.save(**valid_data)
            else:
                serializer.save()
        else:
            serializer.save()

class MediaItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MediaItem.objects.all()
    serializer_class = MediaItemSerializer

class CustomListCreateView(generics.ListCreateAPIView):
    queryset = CustomList.objects.all()
    serializer_class = CustomListSerializer

class CustomListDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomList.objects.all()
    serializer_class = CustomListSerializer

class RecommendationView(APIView):
    def get(self, request):
        # Provide random recommendations for anime
        media_items = MediaItem.objects.filter(category__name='Anime')
        recommendations = random.sample(list(media_items), min(5, len(media_items)))  # Random selection
        serializer = MediaItemSerializer(recommendations, many=True)
        return Response(serializer.data)