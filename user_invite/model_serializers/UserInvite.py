from rest_framework import serializers
from user_invite.models.UserInvite import UserInvite




class UserInviteSerializer(serializers.ModelSerializer):

    class Meta:

        model = UserInvite
        fields = ['user',
                  'url_clicked',
                  'accepted_invite',
                  'room_id']
    

    def create(self , validated_data):

        return UserInvite.objects.create(**validated_data)
    

    def update(self , instance , validated_data):

        instance.user = validated_data.get('user' ,
                                           instance.user)

        instance.url_clicked = validated_data.get('url_clicked' ,
                                                  instance.url_clicked)

        instance.accepted_invite = validated_data.get('accepted_invite' ,
                                                      instance.accepted_invite)

        instance.room_id = validated_data.get('room_id' ,
                                              instance.room_id)
                                              
        instance.save()

        return instance
    