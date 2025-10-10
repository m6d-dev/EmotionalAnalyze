from src.apps.emotions.dtos import EmotionDTO
from src.apps.emotions.models import Emotions
from src.utils.repositories import AbstractRepository


class EmotionsRepository(AbstractRepository[Emotions]):
    model = Emotions
    dto_class = EmotionDTO

emotions_repo = EmotionsRepository()
