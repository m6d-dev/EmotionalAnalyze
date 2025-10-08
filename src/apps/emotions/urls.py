from django.urls import path
from src.apps.emotions.views import EmotionsAnalyzeAPIView

urlpatterns = [
    path("analyze/", EmotionsAnalyzeAPIView.as_view())
]
