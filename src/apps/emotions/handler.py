import json
from typing import Any, Dict
from django.core.files.uploadedfile import InMemoryUploadedFile
from src.apps.emotions.functions import convert_numpy_to_python
from src.apps.emotions.service import EmotionsService, emotions_service
from src.apps.emotions.use_case import (
    AnalyseEmotionUseCase,
    HashImageUseCase,
    hash_img_uc,
    analyze_emotion_uc,
)
from src.apps.emotions.dtos import ImageDTO


class ImageAnalyzeHandler:
    def __init__(
        self,
        hash_image_uc: HashImageUseCase = hash_img_uc,
        analyze_image_uc: AnalyseEmotionUseCase = analyze_emotion_uc,
        service: EmotionsService = emotions_service,
    ):
        self.hash_image_uc = hash_image_uc
        self.analyze_image_uc = analyze_image_uc
        self.service = service

    def handle(self, dto: ImageDTO):
        image_hash: str = self.hash_image_uc.execute(dto=dto)

        instance = self.service.get(hash=image_hash)
        if instance:
            return instance.payload

        instance = self.service.create(
            hash=image_hash, **self.__get_data(image=dto.image)
        )

        return instance.payload

    def __get_data(self, image: InMemoryUploadedFile) -> Dict[str, Any]:
        dto: ImageDTO = ImageDTO(image=image)

        result = self.analyze_image_uc.execute(dto=dto)[0]

        return {"payload": json.dumps(convert_numpy_to_python(result))}
    
    def __validate(self, user_id: int) -> None:
        ...


image_analyze_handler = ImageAnalyzeHandler()
