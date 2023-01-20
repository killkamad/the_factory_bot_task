from django.urls import path
from core.views import RegistrationAPIView, SendMessage, ListMessages, GenerateTokenForTelegram, CheckTokenForTelegram
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('send-message/', SendMessage.as_view(), name='send_message'),
    path('list-messages/', ListMessages.as_view(), name='list_messages'),
    path('generate-token/', GenerateTokenForTelegram.as_view(), name='generate_token'),
    path('check-token/', CheckTokenForTelegram.as_view(), name='check_token'),
]
