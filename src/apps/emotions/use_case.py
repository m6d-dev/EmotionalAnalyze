from src.utils.use_cases import AbstractUseCase
from deepface import DeepFace

class AnalyzeEmotionUseCase(AbstractUseCase):
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

analyze_emotion_uc = AnalyzeEmotionUseCase()