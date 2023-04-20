from django.urls import path
from .views import User_Profile_Update_ViewSet, AllPlant_ViewSet, OnePlant_ViewSet

urlpatterns = [
    path('plants', AllPlant_ViewSet.as_view()),
    path('plants/<int:id', OnePlant_ViewSet.as_view()),
]
