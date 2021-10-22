from rest_framework import serializers
from user_invite.models.Notification import Notification




class NotificationSerializer(serializers.ModelSerializer):


    class Meta:

        model = Notification
        fields = '__all__'


    def create(self , validated_data):

        return Notification.objects.create(**validated_data)


    def update(self , instance , validated_data):

        instance.user = validated_data.get('user' ,
                                           instance.user)

        instance.room = validated_data.get('room' , 
                                           instance.room)

        instance.invite_method = validated_data.get('invite_method' ,
                                                    instance.invite_method)

        instance.status = validated_data.get('status' ,
                                             instance.status)

        instance.target_ct = validated_data.get('target_ct' ,
                                                instance.target_ct)

        instance.target_id = validated_data.get('target_id' ,
                                                instance.target_id)

        instance.title = validated_data.get('title' ,
                                            instance.title)

        instance.body = validated_data.get('body' ,
                                           instance.body)

        instance.notification_type = validated_data.get('notification_type' ,
                                                        instance.notification_type)

        instance.date_time = validated_data.get('date_time' ,
                                                instance.date_time)

        instance.save()
        
        return instance