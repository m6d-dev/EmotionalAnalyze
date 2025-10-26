from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from src.apps.emotions.dtos import ImageDTO
from src.apps.emotions.serializers import PostEmotionsSerializer
from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework.parsers import MultiPartParser, JSONParser
from src.apps.emotions.handler import image_analyze_handler
from rest_framework.permissions import IsAuthenticated


class EmotionsAnalyzeAPIView(APIView):
    permission_classes = (IsAuthenticated, )
    parser_classes = (JSONParser, MultiPartParser)
    serializer_class = PostEmotionsSerializer

    @extend_schema(
        request=PostEmotionsSerializer,
        responses={201: OpenApiResponse(description="Emotion analyzed")},
    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            images = request.FILES.getlist('images')
            res = []
            for image in images:
                res.append(image_analyze_handler.handle(
                    dto=ImageDTO(image=image)
                ))
            return Response(data={"result": res}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
