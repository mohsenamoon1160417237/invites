from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from user_invite.models.UserInvite import UserInvite


@registry.register_document
class UserInviteDocument(Document):

    class Index:
        name = 'notification'
        settings = {
            'number_of_shards' : 1,
            'number_of_replicas' : 0
        }

    class Django:

        model = UserInvite
        fields = [
            'url_clicked',
            'accepted_invite',
            'room_id',
            'id'
        ]