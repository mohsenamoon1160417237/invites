from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from user_invite.models.CommentNotifications import CommentNotifications


@registry.register_document
class CommentNotificationsDocument(Document):

    class Index:

        name = 'comment_notifications'
        settings = {
            'number_of_shards' : 1,
            'number_of_replicas' : 0
        }

    class Django:

        model = CommentNotifications
        fields = ['title',
                  'body',
                  'notification_id',
                  'date_time',
                  'id']
