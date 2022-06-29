from rest_framework import serializers
from accounts.models import CustomUser
from chat.models import Chat


class ChatSerializer(serializers.ModelSerializer):

    class Meta:

        model = Chat
        fields = '__all__'