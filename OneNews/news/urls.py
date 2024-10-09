from django.urls import path
from .views import ShowAllNewsAPIView, AddNewsAPIView, ShowFilerTagsAPIView, ShowFilerTextAPIView



urlpatterns = [
    path('all-news/', ShowAllNewsAPIView.as_view()),
    path('add-news/', AddNewsAPIView.as_view()),
    path('filter-tag/<str:tags>', ShowFilerTagsAPIView.as_view()),
    path('filter-text/<str:text>', ShowFilerTextAPIView.as_view()),
   
    
]