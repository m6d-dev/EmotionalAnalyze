from src.apps.emotions.models import AnalyzedImage
from src.apps.emotions.repository import EmotionsRepository, emotions_repo
from src.utils.services import AbstractService


class EmotionsService(AbstractService[AnalyzedImage]):
    def __init__(self, repository: EmotionsRepository = emotions_repo):
        super().__init__(repository)


emotions_service = EmotionsService()
