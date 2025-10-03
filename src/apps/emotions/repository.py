from src.apps.emotions.models import Emotions
from src.utils.repositories import AbstractRepository


class EmotionsRepository(AbstractRepository[Emotions]):
    model = Emotions


emotions_repo = EmotionsRepository()
