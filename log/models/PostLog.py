from django.db import models
from accounts.models.User import User
from user_invite.models.KeycloakRealm import KeycloakRealm
import datetime


class PostLog(models.Model):

    DRAFT = 'draft'
    PUBLISH = 'publish'
    SCHEDULE = 'schedule'

    STATUS = [
        (DRAFT , 'draft'),
        (PUBLISH , 'publish'),
        (SCHEDULE , 'schedule')
    ]

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='posts')
    title = models.CharField(max_length=30)
    content = models.TextField()
    status = models.CharField(choices=STATUS,
                              max_length=8,
                              default=DRAFT)
    post_time = models.DateTimeField()


    def tags_for_user(self , tag_type):

        return self.tags.filter(posts__user=self.user,
                                type=tag_type).count()

    class Meta:

        ordering = ['-post_time']