from django.urls import path
from .views import CategoryListCreateView, MediaItemListCreateView, MediaItemDetailView, CustomListCreateView, CustomListDetailView, RecommendationView

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category_list_create'),
    path('items/', MediaItemListCreateView.as_view(), name='mediaitem_list_create'),
    path('items/<int:pk>/', MediaItemDetailView.as_view(), name='mediaitem_detail'),
    path('lists/', CustomListCreateView.as_view(), name='custom_list_create'),
    path('lists/<int:pk>/', CustomListDetailView.as_view(), name='custom_list_detail'),
    path('recommendations/', RecommendationView.as_view(), name='recommendations'),
]