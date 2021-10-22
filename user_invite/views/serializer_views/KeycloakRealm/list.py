from user_invite.model_serializers.KeycloakRealm import KeycloakRealmSerializer
from user_invite.models.KeycloakRealm import KeycloakRealm
from rest_framework import generics




class KeycloakRealmList(generics.ListCreateAPIView):

    serializer_class = KeycloakRealmSerializer
    queryset = KeycloakRealm.objects.all()
