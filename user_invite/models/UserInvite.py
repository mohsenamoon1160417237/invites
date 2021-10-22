from django.db import models
from .KeycloakUserEntity import KeycloakUserEntity



class UserInvite(models.Model):

    user = models.ForeignKey(KeycloakUserEntity , 
                             on_delete=models.DO_NOTHING , 
                             related_name='user_invite')

    url_clicked = models.BooleanField(default=False)
    accepted_invite = models.BooleanField(default=False)
    room_id = models.CharField(unique=True , 
                               max_length=100)

    def __str__(self):

        return '{} : {}'.format(self.room_id ,
                                self.invite_option)