from src.apps.emotions.dtos import EmotionDTO
from src.apps.emotions.models import AnalyzedImage
from src.utils.repositories import AbstractRepository


class EmotionsRepository(AbstractRepository[AnalyzedImage]):
    model = AnalyzedImage
    dto_class = EmotionDTO


emotions_repo = EmotionsRepository()
