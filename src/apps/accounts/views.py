from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from src.utils.functions import check_field_confirmed, ensure_otp_cooldown, generate_random_string, get_otp_expire_time, send_confirm_email
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from http import HTTPMethod


class RegistrationAPIView(ViewSet):
    """
    ViewSet for handling user registration.
    """

    authentication_classes = ()
    permission_classes = ()

    def get_serializer_class(self):
        """
        Return the serializer class for registration.
        """
        ...
        
    def step1(self, request, *args, **kwargs):
        """
        Handle user registration.
        """
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            data={
                "data": "Ссылка для подтверждения регистрации отправлена на вашу почту."
            },
            status=status.HTTP_201_CREATED,
        )

    def step2(self, request, *args, **kwargs):
        """
        Handle the second step of user registration.
        """
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)
        account_service.confirm_account_url(serializer.validated_data["confirmation_url"])
        return Response(data={"data": "Ваш адрес электронной почты успешно подтвержден"}, status=status.HTTP_200_OK)
    
    def resend_otp(self, request, *args, **kwargs):
        account = account_service.get(id=kwargs.get("id"))
        
        ensure_otp_cooldown(account)
        check_field_confirmed(account, "email_verified")

        account.otp = generate_random_string(14)
        account.otp_expire_time = get_otp_expire_time()
        account.save()

        send_confirm_email(account.otp, account.email)
        return Response(
            data={
                "data": "Повторная ссылка для подтверждения регистрации отправлена на вашу почту."
            },
            status=status.HTTP_200_OK,
        )

@permission_classes([IsAuthenticated])
@api_view(http_method_names=[HTTPMethod.GET])
def hello(request, *args, **kwargs):
    return Response(data={"data": "Hllo"})

