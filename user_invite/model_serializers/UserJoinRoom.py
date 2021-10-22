from rest_framework import serializers
from user_invite.models.UserJoinRoom import UserJoinRoom



class UserJoinRoomSerializer(serializers.ModelSerializer):


    class Meta:

        model = UserJoinRoom
        fields = '__all__'


    def create(self , validated_data):

        return UserJoinRoom.objects.create(**validated_data)

    def update(self , instance , validated_data):

        instance.user = validated_data.get('user' ,
                                           instance.user)

        instance.room_id = validated_data.get('room_id' , 
                                              instance.room_id)

        instance.date_time_joined = validated_data.get('date_time_joined' ,
                                                       instance.date_time_joined)

        instance.date_time_left = validated_data.get('date_time_left' , 
                                                     instance.date_time_left)

        instance.invite_method = validated_data.get('invite_method' , 
                                                    instance.invite_method)

        instance.save()
        
        return instance