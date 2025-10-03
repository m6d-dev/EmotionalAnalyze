from src.utils.use_cases import AbstractUseCase
from deepface import DeepFace

class AnalyzeEmotionUseCase(AbstractUseCase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def execute(self, *args, **kwargs):
        image = kwargs.get("images")
        if not image:
            return 
        res = DeepFace.analyze(image, actions=['emotion'])
        return res[0]["dominant_emotion"]


analyze_emotion_uc = AnalyzeEmotionUseCase()