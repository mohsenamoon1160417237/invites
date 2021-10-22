from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from user_invite.models.UserJoinRoom import UserJoinRoom


@registry.register_document
class UserJoinRoomDocument(Document):

    class Index:
        name = 'user_join_room'
        settings = {
            'number_of_shards' : 1,
            'number_of_replicas' : 0
        }

    class Django:

        model = UserJoinRoom
        fields = ['room_id',
                  'date_time_joined',
                  'date_time_left',
                  'invite_method']