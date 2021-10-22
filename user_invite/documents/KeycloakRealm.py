from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from user_invite.models.KeycloakRealm import KeycloakRealm


@registry.register_document
class KeycloakRealmDocument(Document):

    class Index:

        name = 'realms'
        settings = {
            'number_of_shards' : 1,
            'number_of_replicas' : 0
        }

    class Django:

        model = KeycloakRealm
        fields = ['id']