from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey





class CommentNotifications(models.Model):

    title = models.CharField(max_length=299)
    body = models.TextField()
    notification_ct = models.ForeignKey(ContentType , 
                                        related_name='notification_obj' ,
                                        on_delete=models.CASCADE)
    
    notification_id = models.PositiveIntegerField(db_index=True)
    notification = GenericForeignKey('notification_ct' ,
                                     'notification_id')
    
    date_time = models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering = ['-date_time']
