from django.db import models
from .KeycloakUserEntity import KeycloakUserEntity
from .KeycloakRealm import KeycloakRealm
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey




class Notification(models.Model):


    SEEN = 'seen'
    NOT_SEEN ='not seen'

    STATUS = [
        (SEEN , 'seen'),
        (NOT_SEEN , 'not seen')
    ]

    user = models.ForeignKey(KeycloakUserEntity , 
                             on_delete=models.CASCADE , 
                             related_name='invite_sent_notification')
    
    room = models.ForeignKey(KeycloakRealm ,
                             on_delete=models.CASCADE , 
                             related_name='invite_sent_notification')
    
    invite_method = models.CharField(max_length=5)

    status = models.CharField(max_length=10 ,
                              choices=STATUS,
                              null=True)

    target_ct = models.ForeignKey(ContentType ,
                                  on_delete=models.CASCADE,
                                  related_name='obj',
                                  null=True)

    target_id = models.PositiveIntegerField(null=True)

    target = GenericForeignKey('target_ct',
                               'target_id')
    
    title = models.CharField(max_length=299 , 
                             default='Invite sent')

    body = models.TextField()

    notification_type = models.CharField(max_length=20 , 
                                         default='sent')

    date_time = models.DateTimeField(auto_now_add=True)
