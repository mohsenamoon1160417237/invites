from django.db import models
from .KeycloakUserEntity import KeycloakUserEntity




class UserJoinRoom(models.Model):

    EMAIL = 'email'
    SMS = 'sms'

    OPTIONS = (
        (EMAIL , 'em'),
        (SMS , 'sm')
    )


    user = models.ForeignKey(KeycloakUserEntity , 
                             on_delete=models.DO_NOTHING , 
                             related_name='user_join')

    room_id = models.CharField(max_length=299 , 
                               null=True , 
                               unique=True)

    date_time_joined = models.DateTimeField()
    date_time_left = models.DateTimeField(null = True)
    invite_method = models.CharField(choices=OPTIONS , 
                                     max_length=5)

                                     