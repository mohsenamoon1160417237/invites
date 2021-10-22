from rest_framework import serializers
from user_invite.models.KeycloakUserEntity import KeycloakUserEntity




class KeycloakUserEntitySerializer(serializers.HyperlinkedModelSerializer):

    realms = serializers.HyperlinkedRelatedField(many=True ,
                                                read_only=True ,
                                                view_name='keycloakrealm-detail')

    user_invite = serializers.HyperlinkedRelatedField(many=True ,
                                                      read_only=True ,
                                                      view_name='userinvite-detail')

    user_join = serializers.HyperlinkedRelatedField(many=True ,
                                                    read_only=True ,
                                                    view_name='userjoin-detail')


    class Meta:

        model = KeycloakUserEntity
        fields = '__all__'