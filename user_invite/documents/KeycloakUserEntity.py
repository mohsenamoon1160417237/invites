from user_invite.models.KeycloakUserEntity import KeycloakUserEntity
from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry


@registry.register_document
class KeycloakUserEntityDocument(Document):

    class Index:

        name = 'user_entities'
        settings = {
            'number_of_shards' : 1,
            'number_of_replicas' : 0
        }

    class Django:

        model = KeycloakUserEntity
        fields = ['id',
                  'email',
                   'phone_number']
