from django.db import models
from src.utils.models import AbstractTimestampsModel

class Emotions(AbstractTimestampsModel):
    images = models.ImageField(upload_to='uploads/')
    class Meta:
        db_table = 'emotion_analyzer'
        default_permissions = ()