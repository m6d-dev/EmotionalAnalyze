from django.db import models
from src.utils.models import AbstractTimestampsModel


class AnalyzedImage(AbstractTimestampsModel):
    hash = models.CharField(max_length=128, verbose_name="Хэш")
    payload = models.JSONField(
        verbose_name="Готовые данные",
    )

    class Meta:
        db_table = "emotion_analyzer"
        default_permissions = ()
