from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from user_invite.models.Notification import Notification


@registry.register_document
class NotificationDocument(Document):

    class Index:

        name = 'notification'
        settings = {
            'number_of_shards' : 1,
            'number_of_replicas' : 0
        }

    class Django:

        model = Notification
        fields = ['invite_method',
                  'status',
                  'target_id',
                  'title',
                  'body',
                  'notification_type',
                  'date_time',
                  'id']