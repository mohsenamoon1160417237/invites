from django.db import models
from .PostLog import PostLog


class PostTag(models.Model):

    NEW = 'new'
    IMPROVED = 'improved'
    FIXED = 'fixed'
    TAG_TYPES =[
        (NEW , 'new'),
        (FIXED , 'fixed'),
        (IMPROVED , 'improved')
    ]

    posts = models.ManyToManyField(PostLog,
                                   related_name='tags')
    type = models.CharField(choices=TAG_TYPES,
                            max_length=20)

    def number_of_posts(self):

        return self.posts.count()



