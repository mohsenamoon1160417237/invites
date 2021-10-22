from rest_framework import serializers
from user_invite.models.KeycloakRealm import KeycloakRealm
from user_invite.models.KeycloakUserEntity import KeycloakUserEntity



class KeycloakRealmSerializer(serializers.HyperlinkedModelSerializer):

    users = serializers.SlugRelatedField(many=True ,
                                         queryset=KeycloakUserEntity.objects.all() ,
                                         slug_field='email')

    class Meta:

        model = KeycloakRealm
        fields = '__all__'