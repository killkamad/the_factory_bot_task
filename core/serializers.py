from django.contrib.auth import get_user_model
from rest_framework import serializers
from core.models import User, Messages


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField()

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'password']

    def save(self):
        user = User.objects.create(
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name']
        )
        user.set_password(self.validated_data['password'])
        user.save()
        return user


class SendMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ('message_body',)


class ListMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Messages
        fields = ('date_time', 'message_body')
