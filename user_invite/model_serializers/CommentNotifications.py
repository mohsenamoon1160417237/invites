from rest_framework import serializers
from user_invite.models.CommentNotifications import CommentNotifications



class CommentNotificationSerializer(serializers.ModelSerializer):

    class Meta:

        model = CommentNotifications
        fields = '__all__'

    def create(self , validated_data):

        return CommentNotifications.objects.create(**validated_data)
