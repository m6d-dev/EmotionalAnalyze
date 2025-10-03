from django.urls import path
from src.apps.emotions.views import EmotionsAnalyzeAPIView

urlpatterns = [
    path("post/", EmotionsAnalyzeAPIView.as_view({"post": "create"}))
]
