from django.urls import path
from .views import PlantListView, PlantDetailView, WishlistListCreateView, WishlistDestroyView

urlpatterns = [
    path('', PlantListView.as_view()),
    path('<int:pk>/', PlantDetailView.as_view()),
    path('wishlist/', WishlistListCreateView.as_view()),
    path('wishlist/<int:pk>', WishlistDestroyView.as_view()),

]