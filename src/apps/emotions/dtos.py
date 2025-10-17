from src.utils.dto import BaseDTO
from django.core.files.uploadedfile import InMemoryUploadedFile
from pydantic import ConfigDict, Json


class EmotionDTO(BaseDTO):
    id: int
    hash: str
    payload: Json


class ImageDTO(BaseDTO):
    image: InMemoryUploadedFile

    model_config = ConfigDict(arbitrary_types_allowed=True)
