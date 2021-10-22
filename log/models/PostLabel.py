from django.db import models
from .PostLog import PostLog
from accounts.models.User import User



class PostLabel(models.Model):

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='labels',
                             null=True)
    post = models.ForeignKey(PostLog,
                             on_delete=models.CASCADE,
                             related_name='labels',
                             null=True)
    name = models.CharField(max_length=30)

    def number_of_posts(self , user_id):

        return self.posts.filter(user__id=user_id).count()

    class Meta:

        unique_together = ['name' , 'user']




