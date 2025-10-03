from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from src.apps.emotions.use_case import analyze_emotion_uc
from src.apps.emotions.serializers import PostEmotionsSerializer
from src.utils.consts import ViewAction

class EmotionsAnalyzeAPIView(ViewSet):
    authentication_classes = ()
    permission_classes = ()


    def get_serializer_class(self):
        """
        Return the serializer class for registration.
        """
        if self.action == ViewAction.CREATE:
            return PostEmotionsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = analyze_emotion_uc.execute(images=request.data.get("images"))
            return Response(data={"result": res}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
