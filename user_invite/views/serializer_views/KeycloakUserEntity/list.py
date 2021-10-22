from user_invite.model_serializers.KeycloakUserEntity import KeycloakUserEntitySerializer
from user_invite.models.KeycloakUserEntity import KeycloakUserEntity
from rest_framework import generics




class KeycloakUserEntityList(generics.ListCreateAPIView):

    serializer_class = KeycloakUserEntitySerializer
    queryset = KeycloakUserEntity.objects.all()
