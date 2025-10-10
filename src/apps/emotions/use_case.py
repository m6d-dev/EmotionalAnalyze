from src.apps.emotions.service import EmotionsService
from src.utils.use_cases import AbstractUseCase
from deepface import DeepFace
from django.core.files.uploadedfile import InMemoryUploadedFile
import hashlib

class AnalyseEmotionUseCase(AbstractUseCase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def execute(self, *args, **kwargs):
        image = kwargs.get("images")
        if not image:
            return 
        try:
            res = DeepFace.analyze(image, actions=['emotion'])
        except ValueError as e:
            return "Не удалось распознать лицо на изображении. Пожалуйста, загрузите фото с видимым лицом."
        return res

class HashImageUseCase(AbstractUseCase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def execute(self, *args, **kwargs) -> str:
        image: InMemoryUploadedFile = kwargs.get("images")
        image_bytes = image.read()

        image_hash: str = hashlib.sha256(image_bytes).hexdigest()

        return image_hash

class FetchAnalysisResultsUseCase(AbstractUseCase):
    def __init__(
        self,
        emotion_service: EmotionsService,
        **kwargs
    ):
        
        self.service: EmotionsService = emotion_service
        super().__init__(**kwargs)

    def execute(self, image_hash: str):
        ...


analyze_emotion_uc = AnalyseEmotionUseCase()
hash_img_uc = HashImageUseCase()