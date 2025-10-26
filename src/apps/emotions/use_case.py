from src.apps.emotions.dtos import ImageDTO
from src.utils.use_cases import AbstractUseCase
from deepface import DeepFace
from rest_framework.serializers import ValidationError
import hashlib


class AnalyseEmotionUseCase(AbstractUseCase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def execute(self, dto: ImageDTO):
        try:
            res = DeepFace.analyze(dto.image, actions=["emotion"])
        except ValueError as e:
            raise ValidationError(
                "Не удалось распознать лицо на изображении. Пожалуйста, загрузите фото с видимым лицом."
            )
        return res


class HashImageUseCase(AbstractUseCase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def execute(self, dto: ImageDTO) -> str:
        image_bytes = dto.image.read()

        image_hash: str = hashlib.sha256(image_bytes).hexdigest()

        return image_hash


analyze_emotion_uc = AnalyseEmotionUseCase()
hash_img_uc = HashImageUseCase()
