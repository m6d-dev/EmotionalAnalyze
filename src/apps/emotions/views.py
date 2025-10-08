from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from src.apps.emotions.use_case import analyze_emotion_uc
from src.apps.emotions.serializers import PostEmotionsSerializer
from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework.parsers import MultiPartParser, JSONParser

class EmotionsAnalyzeAPIView(APIView):
    authentication_classes = ()
    permission_classes = ()
    parser_classes = (JSONParser, MultiPartParser)
    serializer_class = PostEmotionsSerializer

    @extend_schema(
        request=PostEmotionsSerializer,
        responses={201: OpenApiResponse(description="Emotion analyzed")},
    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            res = analyze_emotion_uc.execute(images=request.data.get("images"))
            print(res)
            return Response(data={"result": res}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
