import binascii
import os

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.models import Messages, User
from rest_framework.views import APIView

from .serializers import RegistrationSerializer, SendMessageSerializer, ListMessagesSerializer


class RegistrationAPIView(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = RegistrationSerializer


class SendMessage(CreateAPIView):
    serializer_class = SendMessageSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        if not request.user.telegram_id:
            return Response({"message": "No telegram_id is linked to your account, but your message saved"},
                            status=status.HTTP_202_ACCEPTED)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class ListMessages(ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Messages.objects.all().order_by('-date_time')
    serializer_class = ListMessagesSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class GenerateTokenForTelegram(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        token = binascii.hexlify(os.urandom(20)).decode()
        User.objects.filter(pk=request.user.pk).update(telegram_token=token)
        return Response({'token': f'token{token}'})


class CheckTokenForTelegram(APIView):

    def post(self, request):
        token = request.data.get('token', None)
        chat_id = request.data.get('chat_id', None)
        if token and chat_id:
            user = User.objects.filter(telegram_token=token, telegram_id__isnull=True)
            if user:
                User.objects.filter(telegram_id=chat_id).update(telegram_id=None)  # unlinked existing user if exist
                user.update(telegram_id=chat_id)
                return Response({'message': 'Your chat id was linked'})
        return Response({'message': 'Not valid token'})
